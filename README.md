# MathChain - Blockchain Visualization Application

A Streamlit-based educational blockchain implementation demonstrating core concepts including block structure, Merkle trees, and state transitions.

## Features

- **Block Traversal**: View and edit blocks to demonstrate immutability
- **Merkle Tree Visualization**: Interactive visualization of transaction verification
- **Turing System**: State-based computation demonstration
- **Transaction Management**: Create and manage transactions and blocks

## File Structure

```
mathchain/
├── src/
│   ├── __init__.py
│   ├── core/                    # Core blockchain components
│   │   ├── __init__.py
│   │   ├── transaction.py       # Transaction data structure
│   │   ├── block.py             # Block data structure
│   │   └── blockchain.py        # Blockchain management
│   ├── utils/                   # Utility functions
│   │   ├── __init__.py
│   │   └── merkle_tree.py       # Merkle tree computations
│   └── ui/                      # Streamlit UI components
│       ├── __init__.py
│       ├── block_traversal.py   # Block viewing/editing UI
│       ├── merkle_visualization.py  # Merkle tree visualization
│       └── turing_system.py     # State transition UI
├── app.py                       # Main application
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cherry-aggarwal/MathChain.git
cd MathChain
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Architecture

### Core Components

- **Transaction**: Represents a transfer between two parties
- **Block**: Contains multiple transactions and links to previous block
- **Blockchain**: Manages the chain of blocks and validates integrity

### Utilities

- **Merkle Tree**: Computes Merkle roots and generates visualization data

### UI Components

- **Block Traversal**: Allows viewing and editing blocks to demonstrate how changes break the chain
- **Merkle Visualization**: Shows how transactions are verified using Merkle trees
- **Turing System**: Demonstrates state transitions and account balances

## Key Concepts Demonstrated

1. **Immutability**: Editing a transaction breaks the chain by invalidating hashes
2. **Merkle Trees**: Efficient transaction verification
3. **State Transitions**: Deterministic computation of account balances
4. **Hash Linking**: Each block references the previous block's hash

## Development

The codebase follows clean architecture principles:

- **Separation of Concerns**: Core logic separated from UI
- **Modularity**: Each component has a single responsibility
- **Type Hints**: All functions include type annotations
- **Documentation**: Comprehensive docstrings

## License

MIT License