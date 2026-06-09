"""
Iris Classifier — Minimal PyTorch Training Example
====================================================
Demonstrates a complete training loop for a 3-class tabular classifier.
Intended as a pedagogical example: small, readable, reproducible.
# Customization coverage: `python.instructions.md` enforces style (PEP 8,
# NumPy docstrings, type hints) when editing this file. The `notebook-guardian`
# hook protects notebook reads, and `csv-eda-basica` uses the same dataset
# (`data/sample.csv`) represented in this training example.

Usage
-----
    python src/train_model.py
    python src/train_model.py --seed 99 --epochs 50 --device cpu
"""

import argparse
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset


# ---------------------------------------------------------------------------
# Reproducibility
# ---------------------------------------------------------------------------

def set_seed(seed: int) -> None:
    """Fix all random seeds for reproducible runs.

    Parameters
    ----------
    seed : int
        Integer seed value shared across Python, NumPy, and PyTorch.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    # If CUDA is available, fix it there too
    torch.cuda.manual_seed_all(seed)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

LABEL_MAP: dict[str, int] = {"setosa": 0, "versicolor": 1, "virginica": 2}
DATA_PATH = Path(__file__).parent.parent / "data" / "sample.csv"


def load_data(path: Path) -> tuple[torch.Tensor, torch.Tensor]:
    """Load the iris CSV and return feature and label tensors.

    Parameters
    ----------
    path : Path
        Path to the CSV file with columns:
        sepal_length, sepal_width, petal_length, petal_width, species.

    Returns
    -------
    X : torch.Tensor, shape (N, 4)
        Normalised feature matrix (zero mean, unit variance).
    y : torch.Tensor, shape (N,)
        Integer class labels.
    """
    df = pd.read_csv(path)
    X_np = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]].values
    y_np = df["species"].map(LABEL_MAP).values

    # Normalise features: zero mean, unit variance
    X_np = (X_np - X_np.mean(axis=0)) / (X_np.std(axis=0) + 1e-8)

    X = torch.tensor(X_np, dtype=torch.float32)
    y = torch.tensor(y_np, dtype=torch.long)
    return X, y


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

class IrisClassifier(nn.Module):
    """Two-layer MLP for Iris species classification.

    Parameters
    ----------
    n_features : int
        Number of input features (4 for Iris).
    n_classes : int
        Number of output classes (3 for Iris).
    hidden_dim : int
        Width of the single hidden layer.
    """

    def __init__(
        self,
        n_features: int = 4,
        n_classes: int = 3,
        hidden_dim: int = 16,
    ) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_features, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Run a forward pass.

        Parameters
        ----------
        x : torch.Tensor, shape (batch, n_features)

        Returns
        -------
        torch.Tensor, shape (batch, n_classes)
            Raw logits (before softmax).
        """
        return self.net(x)


# ---------------------------------------------------------------------------
# Training loop
# ---------------------------------------------------------------------------

def train(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    criterion: nn.Module,
    device: torch.device,
) -> float:
    """Run one epoch of training and return the mean loss.

    Parameters
    ----------
    model : nn.Module
    loader : DataLoader
    optimizer : torch.optim.Optimizer
    criterion : nn.Module
        Loss function (CrossEntropyLoss).
    device : torch.device

    Returns
    -------
    float
        Mean loss over all batches in this epoch.
    """
    model.train()
    total_loss = 0.0
    for X_batch, y_batch in loader:
        X_batch, y_batch = X_batch.to(device), y_batch.to(device)
        optimizer.zero_grad()
        logits = model(X_batch)
        loss = criterion(logits, y_batch)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)


def evaluate(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
) -> float:
    """Compute accuracy on the provided data loader.

    Parameters
    ----------
    model : nn.Module
    loader : DataLoader
    device : torch.device

    Returns
    -------
    float
        Fraction of correctly classified samples in [0, 1].
    """
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for X_batch, y_batch in loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            preds = model(X_batch).argmax(dim=1)
            correct += (preds == y_batch).sum().item()
            total += len(y_batch)
    return correct / total


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Parse arguments, load data, train model, and print results."""
    parser = argparse.ArgumentParser(description="Train a minimal Iris classifier.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--epochs", type=int, default=30)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--lr", type=float, default=1e-2)
    # Explicit device argument — alternative would be auto-detect with torch.cuda.is_available()
    parser.add_argument("--device", type=str, default="cpu", choices=["cpu", "cuda"])
    args = parser.parse_args()

    device = torch.device(args.device)
    set_seed(args.seed)

    X, y = load_data(DATA_PATH)
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True)

    model = IrisClassifier().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(1, args.epochs + 1):
        loss = train(model, loader, optimizer, criterion, device)
        if epoch % 10 == 0:
            acc = evaluate(model, loader, device)
            print(f"Epoch {epoch:3d} | loss={loss:.4f} | train_acc={acc:.2%}")

    final_acc = evaluate(model, loader, device)
    print(f"\nFinal training accuracy: {final_acc:.2%}")


if __name__ == "__main__":
    main()
