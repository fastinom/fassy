{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fastinom/fassy/blob/main/objectDetection_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Fw3xy4PqC548"
      },
      "source": [
        "\n",
        "\n",
        "```\n",
        "\n",
        "1.   Praise T Ganyiwa R204436Q\n",
        "\n",
        "2.   Fastion Mateveva R205684K\n",
        "\n",
        "3.   Shamiso Makainganwa R204437W\n",
        "\n",
        "\n",
        "```\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MDM7GlnRWRUA",
        "outputId": "5f5e450b-644b-45bd-afd4-5aaadaf14ea4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "IAYyxCryYD9i"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "efLnz6TmV_-K",
        "outputId": "ff9e496d-338c-4547-a780-f9eb3bfc5ce8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['dance', 'amapiano', 'petit']\n"
          ]
        }
      ],
      "source": [
        "import numpy as np \n",
        "import pandas as pd \n",
        "import matplotlib.pyplot as plt\n",
        "import os\n",
        "\n",
        "dataset_path =os.listdir ('/content/drive/MyDrive/dataset/train')\n",
        "\n",
        "label_types = os.listdir ('/content/drive/MyDrive/dataset/train')\n",
        "print (label_types)  "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "W5pL-NMXY20i"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rUMbt_TuaXbW",
        "outputId": "4e36767a-6843-489f-b161-5542289b0e86"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "        tag                                         video_name\n",
            "0     dance  /content/drive/MyDrive/dataset/train/dance/vid...\n",
            "1     dance  /content/drive/MyDrive/dataset/train/dance/vid...\n",
            "2     dance  /content/drive/MyDrive/dataset/train/dance/vid...\n",
            "3  amapiano  /content/drive/MyDrive/dataset/train/amapiano/...\n",
            "4  amapiano  /content/drive/MyDrive/dataset/train/amapiano/...\n",
            "        tag                                         video_name\n",
            "4  amapiano  /content/drive/MyDrive/dataset/train/amapiano/...\n",
            "5  amapiano  /content/drive/MyDrive/dataset/train/amapiano/...\n",
            "6     petit  /content/drive/MyDrive/dataset/train/petit/vid...\n",
            "7     petit  /content/drive/MyDrive/dataset/train/petit/vid...\n",
            "8     petit  /content/drive/MyDrive/dataset/train/petit/vid...\n"
          ]
        }
      ],
      "source": [
        "rooms = []\n",
        "\n",
        "for item in dataset_path:\n",
        " # Get all the file names\n",
        " all_rooms = os.listdir('/content/drive/MyDrive/dataset/train' + '/' +item)\n",
        "\n",
        " # Add them to the list\n",
        " for room in all_rooms:\n",
        "    rooms.append((item, str('/content/drive/MyDrive/dataset/train' + '/' +item) + '/' + room))\n",
        "    \n",
        "# Build a dataframe        \n",
        "train_df = pd.DataFrame(data=rooms, columns=['tag', 'video_name'])\n",
        "print(train_df.head())\n",
        "print(train_df.tail())"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "MarIpX5rY6BQ"
      },
      "outputs": [],
      "source": [
        "df = train_df.loc[:,['video_name','tag']]\n",
        "df\n",
        "df.to_csv('train.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eCtLXILqZKRd",
        "outputId": "1db3c5e2-1bc7-4463-fcd5-f78d065da80f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['amapiano', 'petit', 'dance']\n",
            "Types of activities found:  3\n",
            "        tag                                         video_name\n",
            "0  amapiano  /content/drive/MyDrive/dataset/test/amapiano/v...\n",
            "1     petit  /content/drive/MyDrive/dataset/test/petit/vid7...\n",
            "2     dance  /content/drive/MyDrive/dataset/test/dance/vid4...\n",
            "        tag                                         video_name\n",
            "0  amapiano  /content/drive/MyDrive/dataset/test/amapiano/v...\n",
            "1     petit  /content/drive/MyDrive/dataset/test/petit/vid7...\n",
            "2     dance  /content/drive/MyDrive/dataset/test/dance/vid4...\n"
          ]
        }
      ],
      "source": [
        "dataset_path = os.listdir('/content/drive/MyDrive/dataset/test')\n",
        "print(dataset_path)\n",
        "\n",
        "room_types = os.listdir('/content/drive/MyDrive/dataset/test')\n",
        "print(\"Types of activities found: \", len(dataset_path))\n",
        "\n",
        "rooms = []\n",
        "\n",
        "for item in dataset_path:\n",
        " # Get all the file names\n",
        " all_rooms = os.listdir('/content/drive/MyDrive/dataset/test' + '/' +item)\n",
        "\n",
        " # Add them to the list\n",
        " for room in all_rooms:\n",
        "    rooms.append((item, str('/content/drive/MyDrive/dataset/test' + '/' +item) + '/' + room))\n",
        "    \n",
        "# Build a dataframe        \n",
        "test_df = pd.DataFrame(data=rooms, columns=['tag', 'video_name'])\n",
        "print(test_df.head())\n",
        "print(test_df.tail())\n",
        "\n",
        "df = test_df.loc[:,['video_name','tag']]\n",
        "df\n",
        "df.to_csv('test.csv')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "vNmE7ZstaHSZ"
      },
      "outputs": [],
      "source": [
        "from tensorflow import keras\n",
        "from imutils import paths\n",
        "\n",
        "import matplotlib.pyplot as plt\n",
        "import tensorflow as tf\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import imageio\n",
        "import cv2\n",
        "import os"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 368
        },
        "id": "24U768VGawkM",
        "outputId": "1647f3a4-8515-4884-933c-1a5e783946d3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Total videos for training: 9\n",
            "Total videos for testing: 3\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0                                         video_name       tag\n",
              "4           4  /content/drive/MyDrive/dataset/train/amapiano/...  amapiano\n",
              "7           7  /content/drive/MyDrive/dataset/train/petit/vid...     petit\n",
              "3           3  /content/drive/MyDrive/dataset/train/amapiano/...  amapiano\n",
              "0           0  /content/drive/MyDrive/dataset/train/dance/vid...     dance\n",
              "6           6  /content/drive/MyDrive/dataset/train/petit/vid...     petit\n",
              "5           5  /content/drive/MyDrive/dataset/train/amapiano/...  amapiano\n",
              "1           1  /content/drive/MyDrive/dataset/train/dance/vid...     dance\n",
              "8           8  /content/drive/MyDrive/dataset/train/petit/vid...     petit\n",
              "2           2  /content/drive/MyDrive/dataset/train/dance/vid...     dance"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f07e9051-babd-4dba-b76e-7f6233cb2264\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>video_name</th>\n",
              "      <th>tag</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/amapiano/...</td>\n",
              "      <td>amapiano</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>7</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/petit/vid...</td>\n",
              "      <td>petit</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/amapiano/...</td>\n",
              "      <td>amapiano</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/dance/vid...</td>\n",
              "      <td>dance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>6</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/petit/vid...</td>\n",
              "      <td>petit</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>5</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/amapiano/...</td>\n",
              "      <td>amapiano</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/dance/vid...</td>\n",
              "      <td>dance</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>8</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/petit/vid...</td>\n",
              "      <td>petit</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>/content/drive/MyDrive/dataset/train/dance/vid...</td>\n",
              "      <td>dance</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f07e9051-babd-4dba-b76e-7f6233cb2264')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-f07e9051-babd-4dba-b76e-7f6233cb2264 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-f07e9051-babd-4dba-b76e-7f6233cb2264');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ],
      "source": [
        "train_df = pd.read_csv(\"train.csv\")\n",
        "test_df = pd.read_csv(\"test.csv\")\n",
        "\n",
        "print(f\"Total videos for training: {len(train_df)}\")\n",
        "print(f\"Total videos for testing: {len(test_df)}\")\n",
        "\n",
        "\n",
        "train_df.sample(9)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VzwVPNRPa-Vk"
      },
      "outputs": [],
      "source": [
        "IMG_SIZE = 224\n",
        "\n",
        "\n",
        "def crop_center_square(frame):\n",
        "    y, x = frame.shape[0:2]\n",
        "    min_dim = min(y, x)\n",
        "    start_x = (x // 2) - (min_dim // 2)\n",
        "    start_y = (y // 2) - (min_dim // 2)\n",
        "    return frame[start_y : start_y + min_dim, start_x : start_x + min_dim]\n",
        "\n",
        "\n",
        "def load_video(path, max_frames=0, resize=(IMG_SIZE, IMG_SIZE)):\n",
        "    cap = cv2.VideoCapture(path)\n",
        "    frames = []\n",
        "    try:\n",
        "        while True:\n",
        "            ret, frame = cap.read()\n",
        "            if not ret:\n",
        "                break\n",
        "            frame = crop_center_square(frame)\n",
        "            frame = cv2.resize(frame, resize)\n",
        "            frame = frame[:, :, [2, 1, 0]]\n",
        "            frames.append(frame)\n",
        "\n",
        "            if len(frames) == max_frames:\n",
        "                break\n",
        "    finally:\n",
        "        cap.release()\n",
        "    return np.array(frames)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "38990b9EcLU7",
        "outputId": "f2a8df60-167e-4154-887a-4987e9809bda"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5\n",
            "87910968/87910968 [==============================] - 0s 0us/step\n"
          ]
        }
      ],
      "source": [
        "def build_feature_extractor():\n",
        "    feature_extractor = keras.applications.InceptionV3(\n",
        "        weights=\"imagenet\",\n",
        "        include_top=False,\n",
        "        pooling=\"avg\",\n",
        "        input_shape=(IMG_SIZE, IMG_SIZE, 3),\n",
        "    )\n",
        "    preprocess_input = keras.applications.inception_v3.preprocess_input\n",
        "\n",
        "    inputs = keras.Input((IMG_SIZE, IMG_SIZE, 3))\n",
        "    preprocessed = preprocess_input(inputs)\n",
        "\n",
        "    outputs = feature_extractor(preprocessed)\n",
        "    return keras.Model(inputs, outputs, name=\"feature_extractor\")\n",
        "\n",
        "\n",
        "feature_extractor = build_feature_extractor()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lUOqnLxbcNht",
        "outputId": "8b017585-5f06-4b9d-aa9e-c14a1b204068"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['amapiano', 'dance', 'petit']\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1],\n",
              "       [1],\n",
              "       [1],\n",
              "       [0],\n",
              "       [0],\n",
              "       [0],\n",
              "       [2],\n",
              "       [2],\n",
              "       [2]])"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ],
      "source": [
        "label_processor = keras.layers.StringLookup(num_oov_indices=0, vocabulary=np.unique(train_df[\"tag\"]))\n",
        "print(label_processor.get_vocabulary())\n",
        "\n",
        "labels = train_df[\"tag\"].values\n",
        "labels = label_processor(labels[..., None]).numpy()\n",
        "labels"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NQK9OXlZe7Rz"
      },
      "outputs": [],
      "source": [
        "#Define hyperparameters\n",
        "\n",
        "IMG_SIZE = 224\n",
        "BATCH_SIZE = 64\n",
        "EPOCHS = 10\n",
        "\n",
        "MAX_SEQ_LENGTH = 20\n",
        "NUM_FEATURES = 2048"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-B9yl4M8fPJ2",
        "outputId": "52941d22-7d84-4913-b8b3-5dba423057ad"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1/1 [==============================] - 2s 2s/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 181ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 175ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 172ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 173ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 151ms/step\n",
            "1/1 [==============================] - 0s 171ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 168ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 172ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 168ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 183ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 171ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 170ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 170ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 171ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 175ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 174ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 168ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 179ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 152ms/step\n",
            "1/1 [==============================] - 0s 150ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 187ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 155ms/step\n",
            "1/1 [==============================] - 0s 171ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 152ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 172ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 154ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 171ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 170ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 175ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 173ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 151ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 153ms/step\n",
            "1/1 [==============================] - 0s 151ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 170ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 162ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 156ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "Frame features in train set: (9, 20, 2048)\n",
            "Frame masks in train set: (9, 20)\n",
            "train_labels in train set: (9, 1)\n",
            "test_labels in train set: (3, 1)\n"
          ]
        }
      ],
      "source": [
        "def prepare_all_videos(df, root_dir):\n",
        "    num_samples = len(df)\n",
        "    video_paths = df[\"video_name\"].values.tolist()\n",
        "    \n",
        "    ##take all classlabels from train_df column named 'tag' and store in labels\n",
        "    labels = df[\"tag\"].values\n",
        "    \n",
        "    #convert classlabels to label encoding\n",
        "    labels = label_processor(labels[..., None]).numpy()\n",
        "\n",
        "    # `frame_masks` and `frame_features` are what we will feed to our sequence model.\n",
        "    # `frame_masks` will contain a bunch of booleans denoting if a timestep is\n",
        "    # masked with padding or not.\n",
        "    frame_masks = np.zeros(shape=(num_samples, MAX_SEQ_LENGTH), dtype=\"bool\") # 145,20\n",
        "    frame_features = np.zeros(shape=(num_samples, MAX_SEQ_LENGTH, NUM_FEATURES), dtype=\"float32\") #145,20,2048\n",
        "\n",
        "    # For each video.\n",
        "    for idx, path in enumerate(video_paths):\n",
        "        # Gather all its frames and add a batch dimension.\n",
        "        frames = load_video(os.path.join(root_dir, path))\n",
        "        frames = frames[None, ...]\n",
        "\n",
        "        # Initialize placeholders to store the masks and features of the current video.\n",
        "        temp_frame_mask = np.zeros(shape=(1, MAX_SEQ_LENGTH,), dtype=\"bool\")\n",
        "        temp_frame_features = np.zeros(\n",
        "            shape=(1, MAX_SEQ_LENGTH, NUM_FEATURES), dtype=\"float32\"\n",
        "        )\n",
        "\n",
        "        # Extract features from the frames of the current video.\n",
        "        for i, batch in enumerate(frames):\n",
        "            video_length = batch.shape[0]\n",
        "            length = min(MAX_SEQ_LENGTH, video_length)\n",
        "            for j in range(length):\n",
        "                temp_frame_features[i, j, :] = feature_extractor.predict(\n",
        "                    batch[None, j, :]\n",
        "                )\n",
        "            temp_frame_mask[i, :length] = 1  # 1 = not masked, 0 = masked\n",
        "\n",
        "        frame_features[idx,] = temp_frame_features.squeeze()\n",
        "        frame_masks[idx,] = temp_frame_mask.squeeze()\n",
        "\n",
        "    return (frame_features, frame_masks), labels\n",
        "\n",
        "\n",
        "train_data, train_labels = prepare_all_videos(train_df, \"train\")\n",
        "test_data, test_labels = prepare_all_videos(test_df, \"test\")\n",
        "\n",
        "print(f\"Frame features in train set: {train_data[0].shape}\")\n",
        "print(f\"Frame masks in train set: {train_data[1].shape}\")\n",
        "\n",
        "\n",
        "\n",
        "print(f\"train_labels in train set: {train_labels.shape}\")\n",
        "\n",
        "print(f\"test_labels in train set: {test_labels.shape}\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uWWCdk65iQab",
        "outputId": "430af7b7-bb37-442b-8d8b-6de201ecd1f7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Epoch 1/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 1.0434 - accuracy: 0.1667\n",
            "Epoch 1: val_loss improved from inf to 1.72131, saving model to ./tmp/video_classifier\n",
            "1/1 [==============================] - 11s 11s/step - loss: 1.0434 - accuracy: 0.1667 - val_loss: 1.7213 - val_accuracy: 0.0000e+00\n",
            "Epoch 2/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 1.0127 - accuracy: 0.6667\n",
            "Epoch 2: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 103ms/step - loss: 1.0127 - accuracy: 0.6667 - val_loss: 1.8808 - val_accuracy: 0.0000e+00\n",
            "Epoch 3/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.9670 - accuracy: 0.5000\n",
            "Epoch 3: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 64ms/step - loss: 0.9670 - accuracy: 0.5000 - val_loss: 1.8837 - val_accuracy: 0.0000e+00\n",
            "Epoch 4/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.6450 - accuracy: 0.8333\n",
            "Epoch 4: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 74ms/step - loss: 0.6450 - accuracy: 0.8333 - val_loss: 1.8968 - val_accuracy: 0.0000e+00\n",
            "Epoch 5/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.8861 - accuracy: 0.6667\n",
            "Epoch 5: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 65ms/step - loss: 0.8861 - accuracy: 0.6667 - val_loss: 1.8676 - val_accuracy: 0.0000e+00\n",
            "Epoch 6/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.8893 - accuracy: 0.6667\n",
            "Epoch 6: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 63ms/step - loss: 0.8893 - accuracy: 0.6667 - val_loss: 1.8295 - val_accuracy: 0.0000e+00\n",
            "Epoch 7/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.9708 - accuracy: 0.5000\n",
            "Epoch 7: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 62ms/step - loss: 0.9708 - accuracy: 0.5000 - val_loss: 1.7796 - val_accuracy: 0.0000e+00\n",
            "Epoch 8/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.7867 - accuracy: 0.5000\n",
            "Epoch 8: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 66ms/step - loss: 0.7867 - accuracy: 0.5000 - val_loss: 1.7464 - val_accuracy: 0.0000e+00\n",
            "Epoch 9/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.8166 - accuracy: 0.6667\n",
            "Epoch 9: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 60ms/step - loss: 0.8166 - accuracy: 0.6667 - val_loss: 1.7365 - val_accuracy: 0.0000e+00\n",
            "Epoch 10/10\n",
            "1/1 [==============================] - ETA: 0s - loss: 0.7051 - accuracy: 0.8333\n",
            "Epoch 10: val_loss did not improve from 1.72131\n",
            "1/1 [==============================] - 0s 64ms/step - loss: 0.7051 - accuracy: 0.8333 - val_loss: 1.7347 - val_accuracy: 0.0000e+00\n",
            "1/1 [==============================] - 0s 29ms/step - loss: 1.1757 - accuracy: 0.3333\n",
            "Test accuracy: 33.33%\n"
          ]
        }
      ],
      "source": [
        "# Utility for our sequence model.\n",
        "def get_sequence_model():\n",
        "    class_vocab = label_processor.get_vocabulary()\n",
        "\n",
        "    frame_features_input = keras.Input((MAX_SEQ_LENGTH, NUM_FEATURES))\n",
        "    mask_input = keras.Input((MAX_SEQ_LENGTH,), dtype=\"bool\")\n",
        "\n",
        "    # Refer to the following tutorial to understand the significance of using `mask`:\n",
        "    # https://keras.io/api/layers/recurrent_layers/gru/\n",
        "    x = keras.layers.GRU(16, return_sequences=True)(frame_features_input, mask=mask_input)\n",
        "    x = keras.layers.GRU(8)(x)\n",
        "    x = keras.layers.Dropout(0.4)(x)\n",
        "    x = keras.layers.Dense(8, activation=\"relu\")(x)\n",
        "    output = keras.layers.Dense(len(class_vocab), activation=\"softmax\")(x)\n",
        "\n",
        "    rnn_model = keras.Model([frame_features_input, mask_input], output)\n",
        "\n",
        "    rnn_model.compile(\n",
        "        loss=\"sparse_categorical_crossentropy\", optimizer=\"adam\", metrics=[\"accuracy\"]\n",
        "    )\n",
        "    return rnn_model\n",
        "\n",
        "EPOCHS = 10\n",
        "# Utility for running experiments.\n",
        "def run_experiment():\n",
        "    filepath = \"./tmp/video_classifier\"\n",
        "    checkpoint = keras.callbacks.ModelCheckpoint(\n",
        "        filepath, save_weights_only=True, save_best_only=True, verbose=1\n",
        "    )\n",
        "\n",
        "    seq_model = get_sequence_model()\n",
        "    history = seq_model.fit(\n",
        "        [train_data[0], train_data[1]],\n",
        "        train_labels,\n",
        "        validation_split=0.3,\n",
        "        epochs=EPOCHS,\n",
        "        callbacks=[checkpoint],\n",
        "    )\n",
        "\n",
        "    seq_model.load_weights(filepath)\n",
        "    _, accuracy = seq_model.evaluate([test_data[0], test_data[1]], test_labels)\n",
        "    print(f\"Test accuracy: {round(accuracy * 100, 2)}%\")\n",
        "\n",
        "    return history, seq_model\n",
        "\n",
        "\n",
        "_, sequence_model = run_experiment()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 799
        },
        "id": "gJiDUX9IihQJ",
        "outputId": "a64c818e-e67b-4ffb-fc89-26735477d4f3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Test video path: /content/drive/MyDrive/dataset/test/amapiano/vid2.mp4\n",
            "1/1 [==============================] - 0s 198ms/step\n",
            "1/1 [==============================] - 0s 165ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 167ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 159ms/step\n",
            "1/1 [==============================] - 0s 166ms/step\n",
            "1/1 [==============================] - 0s 178ms/step\n",
            "1/1 [==============================] - 0s 157ms/step\n",
            "1/1 [==============================] - 0s 158ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 177ms/step\n",
            "1/1 [==============================] - 0s 160ms/step\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 169ms/step\n",
            "1/1 [==============================] - 0s 170ms/step\n",
            "1/1 [==============================] - 0s 161ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 164ms/step\n",
            "1/1 [==============================] - 0s 24ms/step\n",
            "  dance: 54.76%\n",
            "  amapiano: 27.27%\n",
            "  petit: 17.97%\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-17-e97f70122d72>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     34\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Test video path: {test_video}\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     35\u001b[0m \u001b[0mtest_frames\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msequence_prediction\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_video\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 36\u001b[0;31m \u001b[0mto_gif\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtest_frames\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mMAX_SEQ_LENGTH\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-17-e97f70122d72>\u001b[0m in \u001b[0;36mto_gif\u001b[0;34m(images)\u001b[0m\n\u001b[1;32m     28\u001b[0m     \u001b[0mconverted_images\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mimages\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muint8\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     29\u001b[0m     \u001b[0mimageio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmimsave\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"animation.gif\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mconverted_images\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfps\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m10\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 30\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0membed\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0membed_file\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"animation.gif\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     31\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     32\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'embed' is not defined"
          ]
        }
      ],
      "source": [
        "def prepare_single_video(frames):\n",
        "    frames = frames[None, ...]\n",
        "    frame_mask = np.zeros(shape=(1, MAX_SEQ_LENGTH,), dtype=\"bool\")\n",
        "    frame_features = np.zeros(shape=(1, MAX_SEQ_LENGTH, NUM_FEATURES), dtype=\"float32\")\n",
        "\n",
        "    for i, batch in enumerate(frames):\n",
        "        video_length = batch.shape[0]\n",
        "        length = min(MAX_SEQ_LENGTH, video_length)\n",
        "        for j in range(length):\n",
        "            frame_features[i, j, :] = feature_extractor.predict(batch[None, j, :])\n",
        "        frame_mask[i, :length] = 1  # 1 = not masked, 0 = masked\n",
        "\n",
        "    return frame_features, frame_mask\n",
        "\n",
        "\n",
        "def sequence_prediction(path):\n",
        "    class_vocab = label_processor.get_vocabulary()\n",
        "\n",
        "    frames = load_video(os.path.join(\"test\", path))\n",
        "    frame_features, frame_mask = prepare_single_video(frames)\n",
        "    probabilities = sequence_model.predict([frame_features, frame_mask])[0]\n",
        "\n",
        "    for i in np.argsort(probabilities)[::-1]:\n",
        "        print(f\"  {class_vocab[i]}: {probabilities[i] * 100:5.2f}%\")\n",
        "    return frames\n",
        "\n",
        "def to_gif(images):\n",
        "    converted_images = images.astype(np.uint8)\n",
        "    imageio.mimsave(\"animation.gif\", converted_images, fps=10)\n",
        "    return embed.embed_file(\"animation.gif\")\n",
        "\n",
        "\n",
        "test_video = np.random.choice(test_df[\"video_name\"].values.tolist())\n",
        "print(f\"Test video path: {test_video}\")\n",
        "test_frames = sequence_prediction(test_video)\n",
        "to_gif(test_frames[:MAX_SEQ_LENGTH])"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cAKCDO-LkCTZ",
        "outputId": "f4142186-8d9f-49b8-f615-45b715b0249d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"model\"\n",
            "__________________________________________________________________________________________________\n",
            " Layer (type)                   Output Shape         Param #     Connected to                     \n",
            "==================================================================================================\n",
            " input_4 (InputLayer)           [(None, 20, 2048)]   0           []                               \n",
            "                                                                                                  \n",
            " input_5 (InputLayer)           [(None, 20)]         0           []                               \n",
            "                                                                                                  \n",
            " gru (GRU)                      (None, 20, 16)       99168       ['input_4[0][0]',                \n",
            "                                                                  'input_5[0][0]']                \n",
            "                                                                                                  \n",
            " gru_1 (GRU)                    (None, 8)            624         ['gru[0][0]']                    \n",
            "                                                                                                  \n",
            " dropout (Dropout)              (None, 8)            0           ['gru_1[0][0]']                  \n",
            "                                                                                                  \n",
            " dense (Dense)                  (None, 8)            72          ['dropout[0][0]']                \n",
            "                                                                                                  \n",
            " dense_1 (Dense)                (None, 3)            27          ['dense[0][0]']                  \n",
            "                                                                                                  \n",
            "==================================================================================================\n",
            "Total params: 99,891\n",
            "Trainable params: 99,891\n",
            "Non-trainable params: 0\n",
            "__________________________________________________________________________________________________\n"
          ]
        }
      ],
      "source": [
        "sequence_model.summary()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "YPG5mHJ7Ffp9"
      },
      "outputs": [],
      "source": [
        "sequence_model.save('model.h5') "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QisXFXZJF1EN",
        "outputId": "d2dbe88e-acb0-458f-887e-b4c8fac6fe58"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Model: \"model\"\n",
            "__________________________________________________________________________________________________\n",
            " Layer (type)                   Output Shape         Param #     Connected to                     \n",
            "==================================================================================================\n",
            " input_4 (InputLayer)           [(None, 20, 2048)]   0           []                               \n",
            "                                                                                                  \n",
            " input_5 (InputLayer)           [(None, 20)]         0           []                               \n",
            "                                                                                                  \n",
            " gru (GRU)                      (None, 20, 16)       99168       ['input_4[0][0]',                \n",
            "                                                                  'input_5[0][0]']                \n",
            "                                                                                                  \n",
            " gru_1 (GRU)                    (None, 8)            624         ['gru[0][0]']                    \n",
            "                                                                                                  \n",
            " dropout (Dropout)              (None, 8)            0           ['gru_1[0][0]']                  \n",
            "                                                                                                  \n",
            " dense (Dense)                  (None, 8)            72          ['dropout[0][0]']                \n",
            "                                                                                                  \n",
            " dense_1 (Dense)                (None, 3)            27          ['dense[0][0]']                  \n",
            "                                                                                                  \n",
            "==================================================================================================\n",
            "Total params: 99,891\n",
            "Trainable params: 99,891\n",
            "Non-trainable params: 0\n",
            "__________________________________________________________________________________________________\n"
          ]
        }
      ],
      "source": [
        "new_model = tf.keras.models.load_model('model.h5')\n",
        "\n",
        "# Show the model architecture\n",
        "new_model.summary()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}