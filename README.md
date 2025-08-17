### 

<img width="1920" height="1080" alt="A Predictive Analytical Tool For Stress Paterrns" src="https://github.com/user-attachments/assets/ca659f76-14bc-491e-813e-2ffccdb9777b" />





### Problem : 

Considering today’s lifestyle, people just sleep forgetting the benefits sleep provides to the human body. Smart-Yoga Pillow (SaYoPillow) is proposed to help in understanding the relationship between stress and sleep and to fully materialize the idea of “Smart-Sleeping” by proposing an edge device. An edge processor with a model analyzing the physiological changes that occur during sleep along with the sleeping habits is proposed. Based on these changes during sleep, stress prediction for the following day is proposed. The secure transfer of the analyzed stress data along with the average physiological changes to the IoT cloud for storage is implemented. A secure transfer of any data from the cloud to any third-party applications is also proposed. A user interface is provided allowing the user to control the data accessibility and visibility. SaYoPillow is novel, with security features as well as consideration of sleeping habits for stress reduction, with an accuracy of up to 90+.

### Solution:

This Web app will help you to detects a person's stress level by analysing the values of several features using the Decision Tree Classifier.

### Idea: 
Building an application that can detect the presence of a mental stress or the possible causes of mental ailments due to stress by indicating the highly relevant factors. 

### Layout

```
├───images
├───Tabs
│   └───__pycache__
|   └─── home.py
|   └─── data.py
|   └─── predict.py
|   └─── visualize.py
|   └─── about.py
└───__pycache__
└─── main.py
└─── web_functions.py
└─── requirements.txt
└─── Procfile
└─── setup.sh
```


### Note:
**Incase the application demo doesn't start real quick, you can get an idea about how it looks like from the screenshots**

<img width="1287" height="711" alt="Home" src="https://github.com/user-attachments/assets/9e7ee94a-0320-4111-bbdd-9853a1d04f14" />
<img width="1287" height="638" alt="Screenshot 2025-05-21 162358" src="https://github.com/user-attachments/assets/47fe84cb-51d2-4529-9103-0ca3eee74185" />
<img width="1287" height="711" alt="Screenshot 2025-05-21 162411" src="https://github.com/user-attachments/assets/78ebd587-51f6-4d11-b02d-9b77a8e9e55f" />
<img width="1300" height="570" alt="Screenshot 2025-05-21 162322" src="https://github.com/user-attachments/assets/d8563416-cf56-4e73-b745-da659ba5a12b" />



# How to run on the project on your local 



## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

What things you need to install the software and how to install them.

- Python (version 3.9)
- seaborn
-streamlit
- numpy
- matplotlib
- pandas
- scikit_learn

### Installation

1. **Clone the repository:**

    ```bash
   https://github.com/anshumanbehera27/stress-level-detector.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repo
    ```

3. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/Mac
    # or
    .\venv\Scripts\activate  # On Windows
    ```

4. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

   This command installs all the necessary libraries specified in `requirements.txt`.

5. **Run the code using this command;**
     ```bash
    python -m streamlit run app.py 
    ```
  










