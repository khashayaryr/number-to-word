# Number to Word Converter 🔢

This project provides a simple Python function to convert numerical inputs into their English word representations. It can handle numbers up to the trillions.


## 🚀 Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

You only need Python 3.x installed on your system.

## Installation and Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/khashayaryr/number-to-word.git
    ```

2. Navigate to the project's root directory in your terminal `number-to-word`.
    ```bash
    cd number-to-word
    ```

3. Add the current directory to your `PYTHONPATH` to ensure Python can find the `src` module and run the main script:
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    python src/main.py
    ```

## 📂 Project Structure
    ```
    .
    ├── .gitignore                  # Specifies intentionally untracked files to ignore
    ├── README.md                   # This file
    └── src/
        ├── main.py                 # Contains the core logic for converting numbers to words.
        ├── constants.py            # Stores the word representations for numbers under 20, tens, and powers of 1000.
    ```

## 🛠 How It Works

The `num_to_word` function in `main.py` recursively breaks down the input number into smaller parts and uses the predefined word lists in `constants.py` to construct the final word representation.

* Numbers **below 20** are directly mapped from the `under_20` list.
* Numbers **below 100** are handled by combining words from the `tens` list and recursively calling `num_to_word` for the remainder.
* For numbers **100 and above**, the function identifies the largest power of 1000 (hundred, thousand, million, etc.) that is less than or equal to the number, converts the significant part, and then recursively handles the remainder.

---

## 🙏 Contributing

Contributions are always welcome! If you have suggestions for improvements or new features, please feel free to open an issue or submit a pull request.

---

## 📜 License

This project is open-sourced under the MIT License. See the `LICENSE` file (you'll need to create this if you haven't already) for more details.