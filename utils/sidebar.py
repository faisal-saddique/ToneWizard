import streamlit as st

content = '''
# ToneWizard - Magical Tone Changer Tool

![1baa5b39a0ee85bebdafa687ceb0b42c.gif](https://imgtr.ee/images/2023/08/22/1baa5b39a0ee85bebdafa687ceb0b42c.gif)

ToneWizard is a powerful and enchanting tool that allows you to transform the tone of your text into various emotions and styles. Whether you want to add a touch of comedy, drama, romance, excitement, or any other emotion, ToneWizard has got you covered. With its mystical abilities, it can instantly infuse your text with the desired mood, helping you convey your message with a twist of magic.

## Getting Started

To use ToneWizard, follow these simple steps:

1. Input your text in the provided text box.
2. Choose the tone you want to apply from the list of options.
3. Click the "Go" button to witness the transformation.

## Features

- **Wide Range of Tones:** ToneWizard offers an array of tones to choose from, including comedy, drama, documentary, romance, and many more.
- **Real-time Transformation:** Watch as your text is instantly imbued with the selected tone, giving it a whole new dimension.
- **User-Friendly Interface:** The intuitive interface ensures that using ToneWizard is a breeze, even for first-time users.
- **Magical Theme:** The tool's enchanting design and theme create an immersive and captivating experience.

## How It Works

ToneWizard employs advanced language processing techniques to analyze your input text and apply the selected tone. It uses the power of AI to ensure that the tone transformation is seamless and engaging.

## Installation

1. Unzip the folder to your desired location.
2. Install the required dependencies using terminal opened inside the same location: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`

## Contribution

Contributions to ToneWizard are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.

## Support

If you encounter any issues or have questions about ToneWizard, please contact us at support@tonewizard.com or visit our [support page](https://tonewizard.com/support).

## License

This project is licensed under the [MIT License](LICENSE).

---

Thank you for choosing ToneWizard to add a touch of magic to your text! 🌟✨
'''

def sidebar():
    with st.sidebar:
        st.markdown(content)
