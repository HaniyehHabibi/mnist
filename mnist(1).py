{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xLOXFOT5Q40E"
   },
   "source": [
    "##### Copyright 2020 The TensorFlow Authors."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "cellView": "form",
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:37:35.189746Z",
     "iopub.status.busy": "2023-08-28T11:37:35.189254Z",
     "iopub.status.idle": "2023-08-28T11:37:35.192923Z",
     "shell.execute_reply": "2023-08-28T11:37:35.192314Z"
    },
    "id": "iiQkM5ZgQ8r2"
   },
   "outputs": [],
   "source": [
    "#@title Licensed under the Apache License, Version 2.0 (the \"License\");\n",
    "# you may not use this file except in compliance with the License.\n",
    "# You may obtain a copy of the License at\n",
    "#\n",
    "# https://www.apache.org/licenses/LICENSE-2.0\n",
    "#\n",
    "# Unless required by applicable law or agreed to in writing, software\n",
    "# distributed under the License is distributed on an \"AS IS\" BASIS,\n",
    "# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
    "# See the License for the specific language governing permissions and\n",
    "# limitations under the License."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "j6331ZSsQGY3"
   },
   "source": [
    "# MNIST classification"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "i9Jcnb8bQQyd"
   },
   "source": [
    "<table class=\"tfo-notebook-buttons\" align=\"left\">\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://www.tensorflow.org/quantum/tutorials/mnist\"><img src=\"https://www.tensorflow.org/images/tf_logo_32px.png\" />View on TensorFlow.org</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://colab.research.google.com/github/tensorflow/quantum/blob/master/docs/tutorials/mnist.ipynb\"><img src=\"https://www.tensorflow.org/images/colab_logo_32px.png\" />Run in Google Colab</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a target=\"_blank\" href=\"https://github.com/tensorflow/quantum/blob/master/docs/tutorials/mnist.ipynb\"><img src=\"https://www.tensorflow.org/images/GitHub-Mark-32px.png\" />View source on GitHub</a>\n",
    "  </td>\n",
    "  <td>\n",
    "    <a href=\"https://storage.googleapis.com/tensorflow_docs/quantum/docs/tutorials/mnist.ipynb\"><img src=\"https://www.tensorflow.org/images/download_logo_32px.png\" />Download notebook</a>\n",
    "  </td>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "udLObUVeGfTs"
   },
   "source": [
    "This tutorial builds a quantum neural network (QNN) to classify a simplified version of MNIST, similar to the approach used in <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al</a>. The performance of the quantum neural network on this classical data problem is compared with a classical neural network."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "X35qHdh5Gzqg"
   },
   "source": [
    "## Setup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:37:35.196596Z",
     "iopub.status.busy": "2023-08-28T11:37:35.196093Z",
     "iopub.status.idle": "2023-08-28T11:37:58.500100Z",
     "shell.execute_reply": "2023-08-28T11:37:58.499131Z"
    },
    "id": "TorxE5tnkvb2"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tensorflow==2.7.0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached tensorflow-2.7.0-cp39-cp39-manylinux2010_x86_64.whl (489.7 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy>=1.14.5 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.26.0b1)\r\n",
      "Requirement already satisfied: absl-py>=0.4.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.4.0)\r\n",
      "Requirement already satisfied: astunparse>=1.6.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.6.3)\r\n",
      "Requirement already satisfied: libclang>=9.0.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (16.0.6)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting flatbuffers<3.0,>=1.12 (from tensorflow==2.7.0)\r\n",
      "  Using cached flatbuffers-2.0.7-py2.py3-none-any.whl (26 kB)\r\n",
      "Requirement already satisfied: google-pasta>=0.1.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (0.2.0)\r\n",
      "Requirement already satisfied: h5py>=2.9.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (3.9.0)\r\n",
      "Collecting keras-preprocessing>=1.1.1 (from tensorflow==2.7.0)\r\n",
      "  Using cached Keras_Preprocessing-1.1.2-py2.py3-none-any.whl (42 kB)\r\n",
      "Requirement already satisfied: opt-einsum>=2.3.2 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (3.3.0)\r\n",
      "Requirement already satisfied: protobuf>=3.9.2 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (3.20.3)\r\n",
      "Requirement already satisfied: six>=1.12.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.16.0)\r\n",
      "Requirement already satisfied: termcolor>=1.1.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (2.3.0)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: typing-extensions>=3.6.6 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (4.7.1)\r\n",
      "Requirement already satisfied: wheel<1.0,>=0.32.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (0.41.1)\r\n",
      "Requirement already satisfied: wrapt>=1.11.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.14.1)\r\n",
      "Collecting gast<0.5.0,>=0.2.1 (from tensorflow==2.7.0)\r\n",
      "  Using cached gast-0.4.0-py3-none-any.whl (9.8 kB)\r\n",
      "Requirement already satisfied: tensorboard~=2.6 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (2.14.0)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tensorflow-estimator<2.8,~=2.7.0rc0 (from tensorflow==2.7.0)\r\n",
      "  Using cached tensorflow_estimator-2.7.0-py2.py3-none-any.whl (463 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting keras<2.8,>=2.7.0rc0 (from tensorflow==2.7.0)\r\n",
      "  Using cached keras-2.7.0-py2.py3-none-any.whl (1.3 MB)\r\n",
      "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.21.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (0.33.0)\r\n",
      "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorflow==2.7.0) (1.58.0rc1)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: google-auth<3,>=1.6.3 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (2.22.0)\r\n",
      "Requirement already satisfied: google-auth-oauthlib<1.1,>=0.5 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (1.0.0)\r\n",
      "Requirement already satisfied: markdown>=2.6.8 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (3.4.4)\r\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (2.31.0)\r\n",
      "Requirement already satisfied: setuptools>=41.0.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (68.1.2)\r\n",
      "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (0.7.1)\r\n",
      "Requirement already satisfied: werkzeug>=1.0.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from tensorboard~=2.6->tensorflow==2.7.0) (2.3.7)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.0) (5.3.1)\r\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.0) (0.3.0)\r\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.0) (4.9)\r\n",
      "Requirement already satisfied: urllib3<2.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.0) (1.26.16)\r\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth-oauthlib<1.1,>=0.5->tensorboard~=2.6->tensorflow==2.7.0) (1.3.1)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: importlib-metadata>=4.4 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from markdown>=2.6.8->tensorboard~=2.6->tensorflow==2.7.0) (6.8.0)\r\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow==2.7.0) (3.2.0)\r\n",
      "Requirement already satisfied: idna<4,>=2.5 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow==2.7.0) (3.4)\r\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3,>=2.21.0->tensorboard~=2.6->tensorflow==2.7.0) (2023.7.22)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: MarkupSafe>=2.1.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from werkzeug>=1.0.1->tensorboard~=2.6->tensorflow==2.7.0) (2.1.3)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: zipp>=0.5 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard~=2.6->tensorflow==2.7.0) (3.16.2)\r\n",
      "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard~=2.6->tensorflow==2.7.0) (0.5.0)\r\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<1.1,>=0.5->tensorboard~=2.6->tensorflow==2.7.0) (3.2.2)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Installing collected packages: tensorflow-estimator, keras, flatbuffers, keras-preprocessing, gast, tensorflow\r\n",
      "  Attempting uninstall: tensorflow-estimator\r\n",
      "    Found existing installation: tensorflow-estimator 2.14.0rc0\r\n",
      "    Uninstalling tensorflow-estimator-2.14.0rc0:\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Successfully uninstalled tensorflow-estimator-2.14.0rc0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: keras\r\n",
      "    Found existing installation: keras 2.14.0rc0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Uninstalling keras-2.14.0rc0:\r\n",
      "      Successfully uninstalled keras-2.14.0rc0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: flatbuffers\r\n",
      "    Found existing installation: flatbuffers 23.5.26\r\n",
      "    Uninstalling flatbuffers-23.5.26:\r\n",
      "      Successfully uninstalled flatbuffers-23.5.26\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: gast\r\n",
      "    Found existing installation: gast 0.5.4\r\n",
      "    Uninstalling gast-0.5.4:\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Successfully uninstalled gast-0.5.4\r\n",
      "  Attempting uninstall: tensorflow\r\n",
      "    Found existing installation: tensorflow 2.14.0rc0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Uninstalling tensorflow-2.14.0rc0:\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Successfully uninstalled tensorflow-2.14.0rc0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Successfully installed flatbuffers-2.0.7 gast-0.4.0 keras-2.7.0 keras-preprocessing-1.1.2 tensorflow-2.7.0 tensorflow-estimator-2.7.0\r\n"
     ]
    }
   ],
   "source": [
    "!pip install tensorflow==2.7.0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "FxkQA6oblNqI"
   },
   "source": [
    "Install TensorFlow Quantum:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:37:58.504734Z",
     "iopub.status.busy": "2023-08-28T11:37:58.504111Z",
     "iopub.status.idle": "2023-08-28T11:38:15.497443Z",
     "shell.execute_reply": "2023-08-28T11:38:15.496532Z"
    },
    "id": "saFHsRDpkvkH"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting tensorflow-quantum==0.7.2\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached tensorflow_quantum-0.7.2-cp39-cp39-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (10.5 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cirq-core==0.13.1 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached cirq_core-0.13.1-py3-none-any.whl (1.6 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cirq-google>=0.13.1 (from tensorflow-quantum==0.7.2)\r\n",
      "  Obtaining dependency information for cirq-google>=0.13.1 from https://files.pythonhosted.org/packages/7f/44/fd0b117b9663751b8bb11609159b651a691b3bfb1dbffd5e085e4bb3efee/cirq_google-1.2.0-py3-none-any.whl.metadata\r\n",
      "  Using cached cirq_google-1.2.0-py3-none-any.whl.metadata (2.0 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting sympy==1.8 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached sympy-1.8-py3-none-any.whl (6.1 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting googleapis-common-protos==1.52.0 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached googleapis_common_protos-1.52.0-py2.py3-none-any.whl (100 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting google-api-core==1.21.0 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached google_api_core-1.21.0-py2.py3-none-any.whl (90 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting google-auth==1.18.0 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached google_auth-1.18.0-py2.py3-none-any.whl (90 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting protobuf==3.17.3 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached protobuf-3.17.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl (1.0 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting duet~=0.2.0 (from cirq-core==0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Obtaining dependency information for duet~=0.2.0 from https://files.pythonhosted.org/packages/be/95/03c8215f675349ff719cb44cd837c2468fdc0c05f55f523f3cad86bbdcc6/duet-0.2.9-py3-none-any.whl.metadata\r\n",
      "  Using cached duet-0.2.9-py3-none-any.whl.metadata (2.3 kB)\r\n",
      "Requirement already satisfied: matplotlib~=3.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (3.7.2)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting networkx~=2.4 (from cirq-core==0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached networkx-2.8.8-py3-none-any.whl (2.0 MB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy~=1.16 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (1.26.0b1)\r\n",
      "Requirement already satisfied: pandas in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (2.0.3)\r\n",
      "Requirement already satisfied: scipy in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (1.11.2)\r\n",
      "Collecting sortedcontainers~=2.0 (from cirq-core==0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached sortedcontainers-2.4.0-py2.py3-none-any.whl (29 kB)\r\n",
      "Requirement already satisfied: tqdm in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (4.66.1)\r\n",
      "Requirement already satisfied: typing-extensions in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from cirq-core==0.13.1->tensorflow-quantum==0.7.2) (4.7.1)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: requests<3.0.0dev,>=2.18.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-api-core==1.21.0->tensorflow-quantum==0.7.2) (2.31.0)\r\n",
      "Requirement already satisfied: setuptools>=34.0.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-api-core==1.21.0->tensorflow-quantum==0.7.2) (68.1.2)\r\n",
      "Requirement already satisfied: six>=1.10.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-api-core==1.21.0->tensorflow-quantum==0.7.2) (1.16.0)\r\n",
      "Requirement already satisfied: pytz in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-api-core==1.21.0->tensorflow-quantum==0.7.2) (2023.3)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cachetools<5.0,>=2.0.0 (from google-auth==1.18.0->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached cachetools-4.2.4-py3-none-any.whl (10 kB)\r\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth==1.18.0->tensorflow-quantum==0.7.2) (0.3.0)\r\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-auth==1.18.0->tensorflow-quantum==0.7.2) (4.9)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting mpmath>=0.19 (from sympy==1.8->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting google-api-core[grpc]>=1.14.0 (from cirq-google>=0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Obtaining dependency information for google-api-core[grpc]>=1.14.0 from https://files.pythonhosted.org/packages/6e/c4/c3cd048b6cbeba8d9ae50dd7643ac065b85237338aa7501b0efae91eb4d9/google_api_core-2.11.1-py3-none-any.whl.metadata\r\n",
      "  Using cached google_api_core-2.11.1-py3-none-any.whl.metadata (2.7 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting proto-plus>=1.20.0 (from cirq-google>=0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Obtaining dependency information for proto-plus>=1.20.0 from https://files.pythonhosted.org/packages/36/5b/e02636d221917d6fa2a61289b3f16002eb4c93d51c0191ac8e896d527182/proto_plus-1.22.3-py3-none-any.whl.metadata\r\n",
      "  Using cached proto_plus-1.22.3-py3-none-any.whl.metadata (2.2 kB)\r\n",
      "INFO: pip is looking at multiple versions of cirq-google to determine which version is compatible with other requirements. This could take a while.\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cirq-google>=0.13.1 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached cirq_google-1.1.0-py3-none-any.whl (577 kB)\r\n",
      "Collecting google-api-core[grpc]<2.0.0dev,>=1.14.0 (from cirq-google>=0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached google_api_core-1.34.0-py3-none-any.whl (120 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting cirq-google>=0.13.1 (from tensorflow-quantum==0.7.2)\r\n",
      "  Using cached cirq_google-1.0.0-py3-none-any.whl (576 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached cirq_google-0.15.0-py3-none-any.whl (641 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached cirq_google-0.14.1-py3-none-any.whl (541 kB)\r\n",
      "  Using cached cirq_google-0.14.0-py3-none-any.whl (541 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached cirq_google-0.13.1-py3-none-any.whl (437 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "INFO: pip is looking at multiple versions of google-api-core[grpc] to determine which version is compatible with other requirements. This could take a while.\r\n",
      "Collecting google-api-core[grpc]<2.0.0dev,>=1.14.0 (from cirq-google>=0.13.1->tensorflow-quantum==0.7.2)\r\n",
      "  Using cached google_api_core-1.33.2-py3-none-any.whl (115 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.33.1-py3-none-any.whl (115 kB)\r\n",
      "  Using cached google_api_core-1.33.0-py3-none-any.whl (115 kB)\r\n",
      "  Using cached google_api_core-1.32.0-py2.py3-none-any.whl (93 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.31.6-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.31.5-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.31.4-py2.py3-none-any.whl (93 kB)\r\n",
      "INFO: pip is still looking at multiple versions of google-api-core[grpc] to determine which version is compatible with other requirements. This could take a while.\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.31.3-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.31.2-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.31.1-py2.py3-none-any.whl (93 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.31.0-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.30.0-py2.py3-none-any.whl (93 kB)\r\n",
      "INFO: This is taking longer than usual. You might need to provide the dependency resolver with stricter constraints to reduce runtime. See https://pip.pypa.io/warnings/backtracking for guidance. If you want to abort this run, press Ctrl + C.\r\n",
      "  Using cached google_api_core-1.29.0-py2.py3-none-any.whl (93 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.28.0-py2.py3-none-any.whl (92 kB)\r\n",
      "  Using cached google_api_core-1.27.0-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.26.3-py2.py3-none-any.whl (93 kB)\r\n",
      "  Using cached google_api_core-1.26.2-py2.py3-none-any.whl (93 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.26.1-py2.py3-none-any.whl (92 kB)\r\n",
      "  Using cached google_api_core-1.26.0-py2.py3-none-any.whl (92 kB)\r\n",
      "  Using cached google_api_core-1.25.1-py2.py3-none-any.whl (92 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.25.0-py2.py3-none-any.whl (92 kB)\r\n",
      "  Using cached google_api_core-1.24.1-py2.py3-none-any.whl (92 kB)\r\n",
      "  Using cached google_api_core-1.24.0-py2.py3-none-any.whl (91 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.23.0-py2.py3-none-any.whl (91 kB)\r\n",
      "  Using cached google_api_core-1.22.4-py2.py3-none-any.whl (91 kB)\r\n",
      "  Using cached google_api_core-1.22.3-py2.py3-none-any.whl (91 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Using cached google_api_core-1.22.2-py2.py3-none-any.whl (91 kB)\r\n",
      "  Using cached google_api_core-1.22.1-py2.py3-none-any.whl (91 kB)\r\n",
      "  Using cached google_api_core-1.22.0-py2.py3-none-any.whl (91 kB)\r\n",
      "Requirement already satisfied: grpcio<2.0dev,>=1.29.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from google-api-core==1.21.0->tensorflow-quantum==0.7.2) (1.58.0rc1)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: contourpy>=1.0.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (1.1.0)\r\n",
      "Requirement already satisfied: cycler>=0.10 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (0.11.0)\r\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (4.42.1)\r\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (1.4.5)\r\n",
      "Requirement already satisfied: packaging>=20.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (23.1)\r\n",
      "Requirement already satisfied: pillow>=6.2.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (10.0.0)\r\n",
      "Requirement already satisfied: pyparsing<3.1,>=2.3.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (3.0.9)\r\n",
      "Requirement already satisfied: python-dateutil>=2.7 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (2.8.2)\r\n",
      "Requirement already satisfied: importlib-resources>=3.2.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (6.0.1)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from pyasn1-modules>=0.2.1->google-auth==1.18.0->tensorflow-quantum==0.7.2) (0.5.0)\r\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core==1.21.0->tensorflow-quantum==0.7.2) (3.2.0)\r\n",
      "Requirement already satisfied: idna<4,>=2.5 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core==1.21.0->tensorflow-quantum==0.7.2) (3.4)\r\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core==1.21.0->tensorflow-quantum==0.7.2) (1.26.16)\r\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from requests<3.0.0dev,>=2.18.0->google-api-core==1.21.0->tensorflow-quantum==0.7.2) (2023.7.22)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tzdata>=2022.1 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from pandas->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (2023.3)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: zipp>=3.1.0 in /tmpfs/src/tf_docs_env/lib/python3.9/site-packages (from importlib-resources>=3.2.0->matplotlib~=3.0->cirq-core==0.13.1->tensorflow-quantum==0.7.2) (3.16.2)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Using cached duet-0.2.9-py3-none-any.whl (29 kB)\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Installing collected packages: sortedcontainers, mpmath, sympy, protobuf, networkx, duet, cachetools, googleapis-common-protos, google-auth, google-api-core, cirq-core, cirq-google, tensorflow-quantum\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: protobuf\r\n",
      "    Found existing installation: protobuf 3.20.3\r\n",
      "    Uninstalling protobuf-3.20.3:\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Successfully uninstalled protobuf-3.20.3\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: networkx\r\n",
      "    Found existing installation: networkx 3.1\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Uninstalling networkx-3.1:\r\n",
      "      Successfully uninstalled networkx-3.1\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: cachetools\r\n",
      "    Found existing installation: cachetools 5.3.1\r\n",
      "    Uninstalling cachetools-5.3.1:\r\n",
      "      Successfully uninstalled cachetools-5.3.1\r\n",
      "  Attempting uninstall: googleapis-common-protos\r\n",
      "    Found existing installation: googleapis-common-protos 1.60.0\r\n",
      "    Uninstalling googleapis-common-protos-1.60.0:\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      Successfully uninstalled googleapis-common-protos-1.60.0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Attempting uninstall: google-auth\r\n",
      "    Found existing installation: google-auth 2.22.0\r\n",
      "    Uninstalling google-auth-2.22.0:\r\n",
      "      Successfully uninstalled google-auth-2.22.0\r\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\r\n",
      "google-auth-oauthlib 1.0.0 requires google-auth>=2.15.0, but you have google-auth 1.18.0 which is incompatible.\r\n",
      "tensorboard 2.14.0 requires protobuf>=3.19.6, but you have protobuf 3.17.3 which is incompatible.\r\n",
      "tensorflow-datasets 4.9.2 requires protobuf>=3.20, but you have protobuf 3.17.3 which is incompatible.\r\n",
      "tensorflow-hub 0.14.0 requires protobuf>=3.19.6, but you have protobuf 3.17.3 which is incompatible.\r\n",
      "tensorflow-metadata 1.14.0 requires protobuf<4.21,>=3.20.3, but you have protobuf 3.17.3 which is incompatible.\u001b[0m\u001b[31m\r\n",
      "\u001b[0mSuccessfully installed cachetools-4.2.4 cirq-core-0.13.1 cirq-google-0.13.1 duet-0.2.9 google-api-core-1.21.0 google-auth-1.18.0 googleapis-common-protos-1.52.0 mpmath-1.3.0 networkx-2.8.8 protobuf-3.17.3 sortedcontainers-2.4.0 sympy-1.8 tensorflow-quantum-0.7.2\r\n"
     ]
    }
   ],
   "source": [
    "!pip install tensorflow-quantum==0.7.2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:15.501753Z",
     "iopub.status.busy": "2023-08-28T11:38:15.501160Z",
     "iopub.status.idle": "2023-08-28T11:38:15.550943Z",
     "shell.execute_reply": "2023-08-28T11:38:15.550330Z"
    },
    "id": "4Ql5PW-ACO0J"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<module 'pkg_resources' from '/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/pkg_resources/__init__.py'>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Update package resources to account for version changes.\n",
    "import importlib, pkg_resources\n",
    "importlib.reload(pkg_resources)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "hdgMMZEBGqyl"
   },
   "source": [
    "Now import TensorFlow and the module dependencies:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:15.554347Z",
     "iopub.status.busy": "2023-08-28T11:38:15.553799Z",
     "iopub.status.idle": "2023-08-28T11:38:19.373477Z",
     "shell.execute_reply": "2023-08-28T11:38:19.372638Z"
    },
    "id": "enZ300Bflq80"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-08-28 11:38:19.216614: E tensorflow/stream_executor/cuda/cuda_driver.cc:271] failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "import tensorflow_quantum as tfq\n",
    "\n",
    "import cirq\n",
    "import sympy\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import collections\n",
    "\n",
    "# visualization tools\n",
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "from cirq.contrib.svg import SVGCircuit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "b08Mmbs8lr81"
   },
   "source": [
    "## 1. Load the data\n",
    "\n",
    "In this tutorial you will build a binary classifier to distinguish between the digits 3 and 6, following <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al.</a> This section covers the data handling that:\n",
    "\n",
    "- Loads the raw data from Keras.\n",
    "- Filters the dataset to only 3s and 6s.\n",
    "- Downscales the images so they fit can fit in a quantum computer.\n",
    "- Removes any contradictory examples.\n",
    "- Converts the binary images to Cirq circuits.\n",
    "- Converts the Cirq circuits to TensorFlow Quantum circuits. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "pDUdGxn-ojgy"
   },
   "source": [
    "### 1.1 Load the raw data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "xZyGXlaKojgz"
   },
   "source": [
    "Load the MNIST dataset distributed with Keras. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:19.378687Z",
     "iopub.status.busy": "2023-08-28T11:38:19.377393Z",
     "iopub.status.idle": "2023-08-28T11:38:19.972414Z",
     "shell.execute_reply": "2023-08-28T11:38:19.971505Z"
    },
    "id": "d9OSExvCojg0"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz\n",
      "\r",
      "   16384/11490434 [..............................] - ETA: 0s"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 8691712/11490434 [=====================>........] - ETA: 0s"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11493376/11490434 [==============================] - 0s 0us/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11501568/11490434 [==============================] - 0s 0us/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of original training examples: 60000\n",
      "Number of original test examples: 10000\n"
     ]
    }
   ],
   "source": [
    "(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()\n",
    "\n",
    "# Rescale the images from [0,255] to the [0.0,1.0] range.\n",
    "x_train, x_test = x_train[..., np.newaxis]/255.0, x_test[..., np.newaxis]/255.0\n",
    "\n",
    "print(\"Number of original training examples:\", len(x_train))\n",
    "print(\"Number of original test examples:\", len(x_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "fZpbygdGojg3"
   },
   "source": [
    "Filter the dataset to keep just the 3s and 6s,  remove the other classes. At the same time convert the label, `y`, to boolean: `True` for `3` and `False` for 6. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:19.976296Z",
     "iopub.status.busy": "2023-08-28T11:38:19.975620Z",
     "iopub.status.idle": "2023-08-28T11:38:19.979730Z",
     "shell.execute_reply": "2023-08-28T11:38:19.979083Z"
    },
    "id": "hOw68cCZojg4"
   },
   "outputs": [],
   "source": [
    "def filter_36(x, y):\n",
    "    keep = (y == 3) | (y == 6)\n",
    "    x, y = x[keep], y[keep]\n",
    "    y = y == 3\n",
    "    return x,y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:19.982916Z",
     "iopub.status.busy": "2023-08-28T11:38:19.982387Z",
     "iopub.status.idle": "2023-08-28T11:38:20.023868Z",
     "shell.execute_reply": "2023-08-28T11:38:20.023099Z"
    },
    "id": "p-XEU8egGL6q"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of filtered training examples: 12049\n",
      "Number of filtered test examples: 1968\n"
     ]
    }
   ],
   "source": [
    "x_train, y_train = filter_36(x_train, y_train)\n",
    "x_test, y_test = filter_36(x_test, y_test)\n",
    "\n",
    "print(\"Number of filtered training examples:\", len(x_train))\n",
    "print(\"Number of filtered test examples:\", len(x_test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3wyiaP0Xojg_"
   },
   "source": [
    "Show the first example:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.027584Z",
     "iopub.status.busy": "2023-08-28T11:38:20.026993Z",
     "iopub.status.idle": "2023-08-28T11:38:20.283895Z",
     "shell.execute_reply": "2023-08-28T11:38:20.283245Z"
    },
    "id": "j5STP7MbojhA"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.colorbar.Colorbar at 0x7f83f41e8f70>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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7e3tKiwslCTNnz9fgwcPVnl5uSRpyZIl+s53vqPnn39e3//+9/Xaa6/po48+0q9+9atu92m7S7cAALC7X/7yl3ruuefk8Xg0fvx4vfDCC8rNzZUkTZkyRcOHD9eGDRv857/xxht67LHHdODAAV155ZVatWqVZs6c2e3+SNYAANgca9YAANgcyRoAAJsjWQMAYHMkawAAbM4xydrs48h6o8cff1wulyugjR49OtLDCrv3339fs2bNUmZmplwul7Zs2RLwumEYWrlypTIyMtSvXz/l5+dr7969kRlsGF3qc1i4cOF534/p06dHZrBhUl5eruuvv14JCQlKTU3V7Nmz1dDQEHDO6dOnVVRUpEGDBmnAgAGaM2fOeTekcLrufA5Tpkw57/tw3333RWjEsMoRydrs48h6s2uvvVaHDh3ytx07dkR6SGHX3t6unJwcVVZWdvn6qlWr9MILL2jt2rX68MMPddlll6mgoECnT5/u4ZGG16U+B0maPn16wPfj1Vdf7cERht/27dtVVFSknTt3auvWrTpz5oymTZum9vZ2/znLli3TH/7wB73xxhvavn27Dh48qDvuuCOCow697nwOkrR48eKA78OqVasiNGJY1u1HfkTQpEmTjKKiIv/PXq/XyMzMNMrLyyM4qp5XVlZm5OTkRHoYESUp4Gk3Pp/PSE9PN5577jn/sePHjxtut9t49dVXIzDCnvHPn4NhGMaCBQuM2267LSLjiZTDhw8bkozt27cbhnH2//u+ffsab7zxhv+cv/71r4Yko7a2NlLDDLt//hwMwzC+853vGEuWLIncoBBStq+sOzs7VVdXp/z8fP+xmJgY5efnq7a2NoIji4y9e/cqMzNTI0aM0N13362mpqZIDymi9u/fL4/HE/D9SEpKUm5ublR+P2pqapSamqqrrrpK999/v44dOxbpIYVVa2urJCk5OVmSVFdXpzNnzgR8H0aPHq2hQ4f26u/DP38O57zyyitKSUnRmDFjVFpaqlOnTkVieAgB299uNJjHkfVWubm52rBhg6666iodOnRITzzxhG6++Wbt3r1bCQkJkR5eRJx7xJzVx8/1BtOnT9cdd9yh7OxsNTY26tFHH9WMGTNUW1ur2NjYSA8v5Hw+n5YuXarJkydrzJgxks5+H+Li4jRw4MCAc3vz96Grz0GS7rrrLg0bNkyZmZn65JNPtHz5cjU0NOjNN9+M4GgRLNsna/zDjBkz/H8eN26ccnNzNWzYML3++utatGhRBEcGO7jzzjv9fx47dqzGjRunkSNHqqamRlOnTo3gyMKjqKhIu3fvjop9Gxdzoc/h3nvv9f957NixysjI0NSpU9XY2KiRI0f29DBhke2nwYN5HFm0GDhwoL71rW9p3759kR5KxJz7DvD9ON+IESOUkpLSK78fxcXFevvtt7Vt2zYNGTLEfzw9PV2dnZ06fvx4wPm99ftwoc+hK+fuW90bvw/RwPbJOpjHkUWLkydPqrGxURkZGZEeSsRkZ2crPT094PvR1tamDz/8MOq/H59//rmOHTvWq74fhmGouLhYmzdv1p/+9CdlZ2cHvD5hwgT17ds34PvQ0NCgpqamXvV9uNTn0JX6+npJ6lXfh2jiiGnwSz2OLFo89NBDmjVrloYNG6aDBw+qrKxMsbGxmjdvXqSHFlYnT54MqAb279+v+vp6JScna+jQoVq6dKmefvppXXnllcrOztaKFSuUmZmp2bNnR27QYXCxzyE5OVlPPPGE5syZo/T0dDU2Nurhhx/WqFGjVFBQEMFRh1ZRUZE2btyot956SwkJCf516KSkJPXr109JSUlatGiRSkpKlJycrMTERD344IPKy8vTDTfcEOHRh86lPofGxkZt3LhRM2fO1KBBg/TJJ59o2bJluuWWWzRu3LgIjx5BifR29O568cUXjaFDhxpxcXHGpEmTjJ07d0Z6SD1u7ty5RkZGhhEXF2cMHjzYmDt3rrFv375IDyvstm3bZkg6ry1YsMAwjLOXb61YscJIS0sz3G63MXXqVKOhoSGygw6Di30Op06dMqZNm2ZcccUVRt++fY1hw4YZixcvNjweT6SHHVJd/f0lGevXr/ef89VXXxkPPPCAcfnllxv9+/c3br/9duPQoUORG3QYXOpzaGpqMm655RYjOTnZcLvdxqhRo4x///d/N1pbWyM7cASNR2QCAGBztl+zBgAg2pGsAQCwOZI1AAA2R7IGAMDmSNYAANgcyRoAAJsjWQMAYHMkawAAbI5kDQCAzZGsAQCwOZI1AAA29/8B7cZ7Qk9z8/UAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(y_train[0])\n",
    "\n",
    "plt.imshow(x_train[0, :, :, 0])\n",
    "plt.colorbar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "wNS9sVPQojhC"
   },
   "source": [
    "### 1.2 Downscale the images"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "fmmtplIFGL6t"
   },
   "source": [
    "An image size of 28x28 is much too large for current quantum computers. Resize the image down to 4x4:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.287540Z",
     "iopub.status.busy": "2023-08-28T11:38:20.286979Z",
     "iopub.status.idle": "2023-08-28T11:38:20.380688Z",
     "shell.execute_reply": "2023-08-28T11:38:20.380027Z"
    },
    "id": "lbhUdBFWojhE",
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "x_train_small = tf.image.resize(x_train, (4,4)).numpy()\n",
    "x_test_small = tf.image.resize(x_test, (4,4)).numpy()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "pOMd7zIjGL6x"
   },
   "source": [
    "Again, display the first training example—after resize: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.384110Z",
     "iopub.status.busy": "2023-08-28T11:38:20.383546Z",
     "iopub.status.idle": "2023-08-28T11:38:20.648858Z",
     "shell.execute_reply": "2023-08-28T11:38:20.648223Z"
    },
    "id": "YIYOtCRIGL6y",
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<matplotlib.colorbar.Colorbar at 0x7f83f40b3ee0>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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asNutxsFBQXGl19+aTzwwANGly5dDJfLZRiGYdx3333G3LlzvfU//fRTo127dsZLL71kHDhwwMjNzTXat29v7N2717QYWyr2Z555xti0aZNx6NAho7S01Lj77ruN6OhoY//+/a0W8+nTp409e/YYe/bsMSQZixYtMvbs2WMcOXLEMAzDmDt3rnHfffd563/99ddGx44djUcffdQ4cOCAsXTpUiMyMtIoLCxstZibG/vixYuNdevWGf/zP/9j7N2715g9e7YRERFhfPTRR60W80MPPWTExMQYxcXFxrFjx7zlhx9+8NYJxt94c+IOht+3YVz4HWzdutU4fPiw8cUXXxhz5841bDab92TRYPy+mxN3sHzfoS4skv3//u//GlOnTjU6depkOBwOIzMz0zh9+rT3/cOHDxuSjI8//tgwDMOoqKgwbrrpJqNr166G3W43+vfvbzz66KNGdXW1qXG29pGGLakpsQfDUcUXH0f7ZbkY57Rp04xx48Zd0iYpKcmIiooyrr76auPNN99s1Zh/HkdTYn/++eeNa665xoiOjja6du1qpKamGlu2bGnVmP3FK8nnOwzG33hz4g6G37dhNP0IccNo++/bMDj6vK1wxC0AAGEuaOfsAQBAyyDZAwAQ5kj2AACEOZI9AABhjmQPAECYI9kDABDmSPYAAIQ5kj0AAGGOZA8AQJgj2QMAEOZI9gAAhLn/D/T28TK1dJyhAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "print(y_train[0])\n",
    "\n",
    "plt.imshow(x_train_small[0,:,:,0], vmin=0, vmax=1)\n",
    "plt.colorbar()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "gGeF1_qtojhK"
   },
   "source": [
    "### 1.3 Remove contradictory examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "7ZLkq2yeojhL"
   },
   "source": [
    "From section *3.3 Learning to Distinguish Digits* of <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al.</a>, filter the dataset to remove images that are labeled as belonging to both classes.\n",
    "\n",
    "This is not a standard machine-learning procedure, but is included in the interest of following the paper."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.652506Z",
     "iopub.status.busy": "2023-08-28T11:38:20.651922Z",
     "iopub.status.idle": "2023-08-28T11:38:20.659331Z",
     "shell.execute_reply": "2023-08-28T11:38:20.658692Z"
    },
    "id": "LqOPW0C7ojhL"
   },
   "outputs": [],
   "source": [
    "def remove_contradicting(xs, ys):\n",
    "    mapping = collections.defaultdict(set)\n",
    "    orig_x = {}\n",
    "    # Determine the set of labels for each unique image:\n",
    "    for x,y in zip(xs,ys):\n",
    "       orig_x[tuple(x.flatten())] = x\n",
    "       mapping[tuple(x.flatten())].add(y)\n",
    "    \n",
    "    new_x = []\n",
    "    new_y = []\n",
    "    for flatten_x in mapping:\n",
    "      x = orig_x[flatten_x]\n",
    "      labels = mapping[flatten_x]\n",
    "      if len(labels) == 1:\n",
    "          new_x.append(x)\n",
    "          new_y.append(next(iter(labels)))\n",
    "      else:\n",
    "          # Throw out images that match more than one label.\n",
    "          pass\n",
    "    \n",
    "    num_uniq_3 = sum(1 for value in mapping.values() if len(value) == 1 and True in value)\n",
    "    num_uniq_6 = sum(1 for value in mapping.values() if len(value) == 1 and False in value)\n",
    "    num_uniq_both = sum(1 for value in mapping.values() if len(value) == 2)\n",
    "\n",
    "    print(\"Number of unique images:\", len(mapping.values()))\n",
    "    print(\"Number of unique 3s: \", num_uniq_3)\n",
    "    print(\"Number of unique 6s: \", num_uniq_6)\n",
    "    print(\"Number of unique contradicting labels (both 3 and 6): \", num_uniq_both)\n",
    "    print()\n",
    "    print(\"Initial number of images: \", len(xs))\n",
    "    print(\"Remaining non-contradicting unique images: \", len(new_x))\n",
    "    \n",
    "    return np.array(new_x), np.array(new_y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "VMOiJfz_ojhP"
   },
   "source": [
    "The resulting counts do not closely match the reported values, but the exact procedure is not specified.\n",
    "\n",
    "It is also worth noting here that applying filtering contradictory examples at this point does not totally prevent the model from receiving contradictory training examples: the next step binarizes the data which will cause more collisions. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.662508Z",
     "iopub.status.busy": "2023-08-28T11:38:20.662068Z",
     "iopub.status.idle": "2023-08-28T11:38:20.807335Z",
     "shell.execute_reply": "2023-08-28T11:38:20.806651Z"
    },
    "id": "zpnsAssWojhP",
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of unique images: 10387\n",
      "Number of unique 3s:  4912\n",
      "Number of unique 6s:  5426\n",
      "Number of unique contradicting labels (both 3 and 6):  49\n",
      "\n",
      "Initial number of images:  12049\n",
      "Remaining non-contradicting unique images:  10338\n"
     ]
    }
   ],
   "source": [
    "x_train_nocon, y_train_nocon = remove_contradicting(x_train_small, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "SlJ5NVaPojhT"
   },
   "source": [
    "### 1.4 Encode the data as quantum circuits\n",
    "\n",
    "To process images using a quantum computer, <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al.</a> proposed representing each pixel with a qubit, with the state depending on the value of the pixel. The first step is to convert to a binary encoding."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.810829Z",
     "iopub.status.busy": "2023-08-28T11:38:20.810271Z",
     "iopub.status.idle": "2023-08-28T11:38:20.814193Z",
     "shell.execute_reply": "2023-08-28T11:38:20.813558Z"
    },
    "id": "1z8J7OyDojhV"
   },
   "outputs": [],
   "source": [
    "THRESHOLD = 0.5\n",
    "\n",
    "x_train_bin = np.array(x_train_nocon > THRESHOLD, dtype=np.float32)\n",
    "x_test_bin = np.array(x_test_small > THRESHOLD, dtype=np.float32)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "SlJ5NVaPojhU"
   },
   "source": [
    "If you were to remove contradictory images at this point you would be left with only 193, likely not enough for effective training."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.817400Z",
     "iopub.status.busy": "2023-08-28T11:38:20.816889Z",
     "iopub.status.idle": "2023-08-28T11:38:20.891687Z",
     "shell.execute_reply": "2023-08-28T11:38:20.891056Z"
    },
    "id": "1z8J7OyDojhW"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of unique images: 193\n",
      "Number of unique 3s:  80\n",
      "Number of unique 6s:  69\n",
      "Number of unique contradicting labels (both 3 and 6):  44\n",
      "\n",
      "Initial number of images:  10338\n",
      "Remaining non-contradicting unique images:  149\n"
     ]
    }
   ],
   "source": [
    "_ = remove_contradicting(x_train_bin, y_train_nocon)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "oLyxS9KlojhZ"
   },
   "source": [
    "The qubits at pixel indices with values that exceed a threshold, are rotated through an $X$ gate."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:20.894983Z",
     "iopub.status.busy": "2023-08-28T11:38:20.894455Z",
     "iopub.status.idle": "2023-08-28T11:38:22.815496Z",
     "shell.execute_reply": "2023-08-28T11:38:22.814724Z"
    },
    "id": "aOu_3-3ZGL61"
   },
   "outputs": [],
   "source": [
    "def convert_to_circuit(image):\n",
    "    \"\"\"Encode truncated classical image into quantum datapoint.\"\"\"\n",
    "    values = np.ndarray.flatten(image)\n",
    "    qubits = cirq.GridQubit.rect(4, 4)\n",
    "    circuit = cirq.Circuit()\n",
    "    for i, value in enumerate(values):\n",
    "        if value:\n",
    "            circuit.append(cirq.X(qubits[i]))\n",
    "    return circuit\n",
    "\n",
    "\n",
    "x_train_circ = [convert_to_circuit(x) for x in x_train_bin]\n",
    "x_test_circ = [convert_to_circuit(x) for x in x_test_bin]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "zSCXqzOzojhd"
   },
   "source": [
    "Here is the circuit created for the first example (circuit diagrams do not show qubits with zero gates):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:22.819332Z",
     "iopub.status.busy": "2023-08-28T11:38:22.818678Z",
     "iopub.status.idle": "2023-08-28T11:38:22.860451Z",
     "shell.execute_reply": "2023-08-28T11:38:22.859792Z"
    },
    "id": "w3POmUEUojhe",
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "data": {
      "image/svg+xml": [
       "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"169.517734375\" height=\"100.0\"><line x1=\"34.7588671875\" x2=\"139.517734375\" y1=\"25.0\" y2=\"25.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"34.7588671875\" x2=\"139.517734375\" y1=\"75.0\" y2=\"75.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><rect x=\"10.0\" y=\"5.0\" width=\"49.517734375\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"34.7588671875\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(2, 2): </text><rect x=\"10.0\" y=\"55.0\" width=\"49.517734375\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"34.7588671875\" y=\"75.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(3, 1): </text><rect x=\"79.517734375\" y=\"5.0\" width=\"40\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"99.517734375\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"18px\" font-family=\"Arial\">X</text><rect x=\"79.517734375\" y=\"55.0\" width=\"40\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"99.517734375\" y=\"75.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"18px\" font-family=\"Arial\">X</text></svg>"
      ],
      "text/plain": [
       "<cirq.contrib.svg.svg.SVGCircuit at 0x7f83f40476a0>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "SVGCircuit(x_train_circ[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "AEQMxCcBojhg"
   },
   "source": [
    "Compare this circuit to the indices where the image value exceeds the threshold:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:22.863788Z",
     "iopub.status.busy": "2023-08-28T11:38:22.863248Z",
     "iopub.status.idle": "2023-08-28T11:38:22.868216Z",
     "shell.execute_reply": "2023-08-28T11:38:22.867567Z"
    },
    "id": "TBIsiXdtojhh"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 2],\n",
       "       [3, 1]])"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bin_img = x_train_bin[0,:,:,0]\n",
    "indices = np.array(np.where(bin_img)).T\n",
    "indices"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "mWZ24w1Oojhk"
   },
   "source": [
    "Convert these `Cirq` circuits to tensors for `tfq`:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:22.871473Z",
     "iopub.status.busy": "2023-08-28T11:38:22.870958Z",
     "iopub.status.idle": "2023-08-28T11:38:28.471383Z",
     "shell.execute_reply": "2023-08-28T11:38:28.470443Z"
    },
    "id": "IZStEMk4ojhk"
   },
   "outputs": [],
   "source": [
    "x_train_tfcirc = tfq.convert_to_tensor(x_train_circ)\n",
    "x_test_tfcirc = tfq.convert_to_tensor(x_test_circ)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "4USiqeOqGL67"
   },
   "source": [
    "## 2. Quantum neural network\n",
    "\n",
    "There is little guidance for a quantum circuit structure that classifies images. Since the classification is based on the expectation of the readout qubit, <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al.</a> propose using two qubit gates, with the readout qubit always acted upon. This is similar in some ways to running small a <a href=\"https://arxiv.org/abs/1511.06464\" class=\"external\">Unitary RNN</a> across the pixels."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "knIzawEeojho"
   },
   "source": [
    "### 2.1 Build the model circuit\n",
    "\n",
    "This following example shows this layered approach. Each layer uses *n* instances of the same gate, with each of the data qubits acting on the readout qubit.\n",
    "\n",
    "Start with a simple class that will add a layer of these gates to a circuit:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:28.475719Z",
     "iopub.status.busy": "2023-08-28T11:38:28.475048Z",
     "iopub.status.idle": "2023-08-28T11:38:28.480014Z",
     "shell.execute_reply": "2023-08-28T11:38:28.479331Z"
    },
    "id": "-hjxxgU5ojho"
   },
   "outputs": [],
   "source": [
    "class CircuitLayerBuilder():\n",
    "    def __init__(self, data_qubits, readout):\n",
    "        self.data_qubits = data_qubits\n",
    "        self.readout = readout\n",
    "    \n",
    "    def add_layer(self, circuit, gate, prefix):\n",
    "        for i, qubit in enumerate(self.data_qubits):\n",
    "            symbol = sympy.Symbol(prefix + '-' + str(i))\n",
    "            circuit.append(gate(qubit, self.readout)**symbol)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "Sjo5hANFojhr"
   },
   "source": [
    "Build an example circuit layer to see how it looks:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:28.483205Z",
     "iopub.status.busy": "2023-08-28T11:38:28.482801Z",
     "iopub.status.idle": "2023-08-28T11:38:28.616410Z",
     "shell.execute_reply": "2023-08-28T11:38:28.615729Z"
    },
    "id": "SzXWOpUGojhs"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "findfont: Font family 'Arial' not found.\n"
     ]
    },
    {
     "data": {
      "image/svg+xml": [
       "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"522.59953125\" height=\"250.0\"><line x1=\"39.810625\" x2=\"492.59953125000004\" y1=\"25.0\" y2=\"25.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"39.810625\" x2=\"492.59953125000004\" y1=\"75.0\" y2=\"75.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"39.810625\" x2=\"492.59953125000004\" y1=\"125.0\" y2=\"125.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"39.810625\" x2=\"492.59953125000004\" y1=\"175.0\" y2=\"175.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"39.810625\" x2=\"492.59953125000004\" y1=\"225.0\" y2=\"225.0\" stroke=\"#1967d2\" stroke-width=\"1\" /><line x1=\"129.99353515625\" x2=\"129.99353515625\" y1=\"25.0\" y2=\"75.0\" stroke=\"black\" stroke-width=\"3\" /><line x1=\"230.73810546875004\" x2=\"230.73810546875004\" y1=\"25.0\" y2=\"125.0\" stroke=\"black\" stroke-width=\"3\" /><line x1=\"331.48267578125007\" x2=\"331.48267578125007\" y1=\"25.0\" y2=\"175.0\" stroke=\"black\" stroke-width=\"3\" /><line x1=\"432.22724609375007\" x2=\"432.22724609375007\" y1=\"25.0\" y2=\"225.0\" stroke=\"black\" stroke-width=\"3\" /><rect x=\"10.0\" y=\"5.0\" width=\"59.62125\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"39.810625\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(-1, -1): </text><rect x=\"10.0\" y=\"55.0\" width=\"59.62125\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"39.810625\" y=\"75.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(0, 0): </text><rect x=\"10.0\" y=\"105.0\" width=\"59.62125\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"39.810625\" y=\"125.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(1, 0): </text><rect x=\"10.0\" y=\"155.0\" width=\"59.62125\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"39.810625\" y=\"175.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(2, 0): </text><rect x=\"10.0\" y=\"205.0\" width=\"59.62125\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"0\" /><text x=\"39.810625\" y=\"225.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">(3, 0): </text><rect x=\"89.62125\" y=\"55.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"129.99353515625\" y=\"75.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX^(xx-0)</text><rect x=\"89.62125\" y=\"5.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"129.99353515625\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX</text><rect x=\"190.36582031250003\" y=\"105.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"230.73810546875004\" y=\"125.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX^(xx-1)</text><rect x=\"190.36582031250003\" y=\"5.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"230.73810546875004\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX</text><rect x=\"291.11039062500004\" y=\"155.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"331.48267578125007\" y=\"175.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX^(xx-2)</text><rect x=\"291.11039062500004\" y=\"5.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"331.48267578125007\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX</text><rect x=\"391.85496093750004\" y=\"205.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"432.22724609375007\" y=\"225.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX^(xx-3)</text><rect x=\"391.85496093750004\" y=\"5.0\" width=\"80.74457031250002\" height=\"40\" stroke=\"black\" fill=\"white\" stroke-width=\"1\" /><text x=\"432.22724609375007\" y=\"25.0\" dominant-baseline=\"middle\" text-anchor=\"middle\" font-size=\"14px\" font-family=\"Arial\">XX</text></svg>"
      ],
      "text/plain": [
       "<cirq.contrib.svg.svg.SVGCircuit at 0x7f83da58fa00>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "demo_builder = CircuitLayerBuilder(data_qubits = cirq.GridQubit.rect(4,1),\n",
    "                                   readout=cirq.GridQubit(-1,-1))\n",
    "\n",
    "circuit = cirq.Circuit()\n",
    "demo_builder.add_layer(circuit, gate = cirq.XX, prefix='xx')\n",
    "SVGCircuit(circuit)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "T-QhPE1pojhu"
   },
   "source": [
    "Now build a two-layered model, matching the data-circuit size, and include the preparation and readout operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:28.619732Z",
     "iopub.status.busy": "2023-08-28T11:38:28.619160Z",
     "iopub.status.idle": "2023-08-28T11:38:28.624459Z",
     "shell.execute_reply": "2023-08-28T11:38:28.623740Z"
    },
    "id": "JiALbpwRGL69"
   },
   "outputs": [],
   "source": [
    "def create_quantum_model():\n",
    "    \"\"\"Create a QNN model circuit and readout operation to go along with it.\"\"\"\n",
    "    data_qubits = cirq.GridQubit.rect(4, 4)  # a 4x4 grid.\n",
    "    readout = cirq.GridQubit(-1, -1)         # a single qubit at [-1,-1]\n",
    "    circuit = cirq.Circuit()\n",
    "    \n",
    "    # Prepare the readout qubit.\n",
    "    circuit.append(cirq.X(readout))\n",
    "    circuit.append(cirq.H(readout))\n",
    "    \n",
    "    builder = CircuitLayerBuilder(\n",
    "        data_qubits = data_qubits,\n",
    "        readout=readout)\n",
    "\n",
    "    # Then add layers (experiment by adding more).\n",
    "    builder.add_layer(circuit, cirq.XX, \"xx1\")\n",
    "    builder.add_layer(circuit, cirq.ZZ, \"zz1\")\n",
    "\n",
    "    # Finally, prepare the readout qubit.\n",
    "    circuit.append(cirq.H(readout))\n",
    "\n",
    "    return circuit, cirq.Z(readout)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:28.627512Z",
     "iopub.status.busy": "2023-08-28T11:38:28.626985Z",
     "iopub.status.idle": "2023-08-28T11:38:28.641975Z",
     "shell.execute_reply": "2023-08-28T11:38:28.641277Z"
    },
    "id": "2QZvVh7vojhx"
   },
   "outputs": [],
   "source": [
    "model_circuit, model_readout = create_quantum_model()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "LY7vbY6yfABE"
   },
   "source": [
    "### 2.2 Wrap the model-circuit in a tfq-keras model\n",
    "\n",
    "Build the Keras model with the quantum components. This model is fed the \"quantum data\", from `x_train_circ`, that encodes the classical data. It uses a *Parametrized Quantum Circuit* layer, `tfq.layers.PQC`, to train the model circuit, on the quantum data.\n",
    "\n",
    "To classify these images, <a href=\"https://arxiv.org/pdf/1802.06002.pdf\" class=\"external\">Farhi et al.</a> proposed taking the expectation of a readout qubit in a parameterized circuit. The expectation returns a value between 1 and -1."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:28.645092Z",
     "iopub.status.busy": "2023-08-28T11:38:28.644651Z",
     "iopub.status.idle": "2023-08-28T11:38:29.903436Z",
     "shell.execute_reply": "2023-08-28T11:38:29.902482Z"
    },
    "id": "ZYdf_KOxojh0"
   },
   "outputs": [],
   "source": [
    "# Build the Keras model.\n",
    "model = tf.keras.Sequential([\n",
    "    # The input is the data-circuit, encoded as a tf.string\n",
    "    tf.keras.layers.Input(shape=(), dtype=tf.string),\n",
    "    # The PQC layer returns the expected value of the readout gate, range [-1,1].\n",
    "    tfq.layers.PQC(model_circuit, model_readout),\n",
    "])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "jz-FbVc9ojh3"
   },
   "source": [
    "Next, describe the training procedure to the model, using the `compile` method.\n",
    "\n",
    "Since the the expected readout is in the range `[-1,1]`, optimizing the hinge loss is a somewhat natural fit. \n",
    "\n",
    "Note: Another valid approach would be to shift the output range to `[0,1]`, and treat it as the probability the model assigns to class `3`. This could be used with a standard a `tf.losses.BinaryCrossentropy` loss.\n",
    "\n",
    "To use the hinge loss here you need to make two small adjustments. First convert the labels, `y_train_nocon`, from boolean to `[-1,1]`, as expected by the hinge loss."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.907664Z",
     "iopub.status.busy": "2023-08-28T11:38:29.907114Z",
     "iopub.status.idle": "2023-08-28T11:38:29.910845Z",
     "shell.execute_reply": "2023-08-28T11:38:29.910185Z"
    },
    "id": "CgMNkC1Fojh5"
   },
   "outputs": [],
   "source": [
    "y_train_hinge = 2.0*y_train_nocon-1.0\n",
    "y_test_hinge = 2.0*y_test-1.0"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "5nwnveDiojh7"
   },
   "source": [
    "Second, use a custiom `hinge_accuracy` metric that correctly handles `[-1, 1]` as the `y_true` labels argument. \n",
    "`tf.losses.BinaryAccuracy(threshold=0.0)` expects `y_true` to be a boolean, and so can't be used with hinge loss)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.914236Z",
     "iopub.status.busy": "2023-08-28T11:38:29.913681Z",
     "iopub.status.idle": "2023-08-28T11:38:29.917567Z",
     "shell.execute_reply": "2023-08-28T11:38:29.916944Z"
    },
    "id": "3XKtZ_TEojh8"
   },
   "outputs": [],
   "source": [
    "def hinge_accuracy(y_true, y_pred):\n",
    "    y_true = tf.squeeze(y_true) > 0.0\n",
    "    y_pred = tf.squeeze(y_pred) > 0.0\n",
    "    result = tf.cast(y_true == y_pred, tf.float32)\n",
    "\n",
    "    return tf.reduce_mean(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.920689Z",
     "iopub.status.busy": "2023-08-28T11:38:29.920169Z",
     "iopub.status.idle": "2023-08-28T11:38:29.931138Z",
     "shell.execute_reply": "2023-08-28T11:38:29.930467Z"
    },
    "id": "FlpETlLRojiA"
   },
   "outputs": [],
   "source": [
    "model.compile(\n",
    "    loss=tf.keras.losses.Hinge(),\n",
    "    optimizer=tf.keras.optimizers.Adam(),\n",
    "    metrics=[hinge_accuracy])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.934262Z",
     "iopub.status.busy": "2023-08-28T11:38:29.933736Z",
     "iopub.status.idle": "2023-08-28T11:38:29.937867Z",
     "shell.execute_reply": "2023-08-28T11:38:29.937221Z"
    },
    "id": "jkHq2RstojiC"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " pqc (PQC)                   (None, 1)                 32        \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 32\n",
      "Trainable params: 32\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(model.summary())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "lsuOzDYblA9s"
   },
   "source": [
    "### Train the quantum model\n",
    "\n",
    "Now train the model—this takes about 45 min. If you don't want to wait that long, use a small subset of the data (set `NUM_EXAMPLES=500`, below). This doesn't really affect the model's progress during training (it only has 32 parameters, and doesn't need much data to constrain these). Using fewer examples just ends training earlier (5min), but runs long enough to show that it is making progress in the validation logs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.941050Z",
     "iopub.status.busy": "2023-08-28T11:38:29.940547Z",
     "iopub.status.idle": "2023-08-28T11:38:29.943758Z",
     "shell.execute_reply": "2023-08-28T11:38:29.943140Z"
    },
    "id": "n8vuQpSLlBV2"
   },
   "outputs": [],
   "source": [
    "EPOCHS = 3\n",
    "BATCH_SIZE = 32\n",
    "\n",
    "NUM_EXAMPLES = len(x_train_tfcirc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.946831Z",
     "iopub.status.busy": "2023-08-28T11:38:29.946310Z",
     "iopub.status.idle": "2023-08-28T11:38:29.949942Z",
     "shell.execute_reply": "2023-08-28T11:38:29.949311Z"
    },
    "id": "qJnNG-3JojiI"
   },
   "outputs": [],
   "source": [
    "x_train_tfcirc_sub = x_train_tfcirc[:NUM_EXAMPLES]\n",
    "y_train_hinge_sub = y_train_hinge[:NUM_EXAMPLES]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "QMSdgGC1GL7D"
   },
   "source": [
    "Training this model to convergence should achieve >85% accuracy on the test set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:38:29.953180Z",
     "iopub.status.busy": "2023-08-28T11:38:29.952636Z",
     "iopub.status.idle": "2023-08-28T11:41:43.655936Z",
     "shell.execute_reply": "2023-08-28T11:41:43.655145Z"
    },
    "id": "Ya9qP3KkojiM"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      "  1/324 [..............................] - ETA: 4:03 - loss: 1.0036 - hinge_accuracy: 0.4688"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  2/324 [..............................] - ETA: 1:02 - loss: 1.0006 - hinge_accuracy: 0.5156"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  3/324 [..............................] - ETA: 1:00 - loss: 0.9981 - hinge_accuracy: 0.5521"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  4/324 [..............................] - ETA: 1:00 - loss: 1.0026 - hinge_accuracy: 0.5234"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  5/324 [..............................] - ETA: 1:00 - loss: 1.0011 - hinge_accuracy: 0.5500"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  6/324 [..............................] - ETA: 59s - loss: 0.9993 - hinge_accuracy: 0.5625 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  7/324 [..............................] - ETA: 59s - loss: 1.0013 - hinge_accuracy: 0.5491"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  8/324 [..............................] - ETA: 59s - loss: 1.0008 - hinge_accuracy: 0.5508"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  9/324 [..............................] - ETA: 59s - loss: 0.9990 - hinge_accuracy: 0.5729"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 10/324 [..............................] - ETA: 59s - loss: 1.0000 - hinge_accuracy: 0.5688"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 11/324 [>.............................] - ETA: 58s - loss: 1.0000 - hinge_accuracy: 0.5625"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 12/324 [>.............................] - ETA: 58s - loss: 1.0006 - hinge_accuracy: 0.5573"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 13/324 [>.............................] - ETA: 58s - loss: 0.9998 - hinge_accuracy: 0.5625"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 14/324 [>.............................] - ETA: 58s - loss: 0.9995 - hinge_accuracy: 0.5603"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 15/324 [>.............................] - ETA: 58s - loss: 0.9978 - hinge_accuracy: 0.5708"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 16/324 [>.............................] - ETA: 57s - loss: 0.9972 - hinge_accuracy: 0.5762"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 17/324 [>.............................] - ETA: 57s - loss: 0.9972 - hinge_accuracy: 0.5699"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 18/324 [>.............................] - ETA: 57s - loss: 0.9976 - hinge_accuracy: 0.5642"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 19/324 [>.............................] - ETA: 57s - loss: 0.9976 - hinge_accuracy: 0.5592"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 20/324 [>.............................] - ETA: 57s - loss: 0.9974 - hinge_accuracy: 0.5562"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 21/324 [>.............................] - ETA: 57s - loss: 0.9974 - hinge_accuracy: 0.5551"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 22/324 [=>............................] - ETA: 56s - loss: 0.9978 - hinge_accuracy: 0.5483"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 23/324 [=>............................] - ETA: 56s - loss: 0.9977 - hinge_accuracy: 0.5476"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 24/324 [=>............................] - ETA: 56s - loss: 0.9977 - hinge_accuracy: 0.5443"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 25/324 [=>............................] - ETA: 56s - loss: 0.9978 - hinge_accuracy: 0.5412"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 26/324 [=>............................] - ETA: 56s - loss: 0.9971 - hinge_accuracy: 0.5469"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 27/324 [=>............................] - ETA: 55s - loss: 0.9971 - hinge_accuracy: 0.5451"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 28/324 [=>............................] - ETA: 55s - loss: 0.9976 - hinge_accuracy: 0.5379"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 29/324 [=>............................] - ETA: 55s - loss: 0.9979 - hinge_accuracy: 0.5323"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 30/324 [=>............................] - ETA: 55s - loss: 0.9980 - hinge_accuracy: 0.5292"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 31/324 [=>............................] - ETA: 55s - loss: 0.9979 - hinge_accuracy: 0.5292"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 32/324 [=>............................] - ETA: 55s - loss: 0.9975 - hinge_accuracy: 0.5312"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 33/324 [==>...........................] - ETA: 54s - loss: 0.9972 - hinge_accuracy: 0.5303"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 34/324 [==>...........................] - ETA: 54s - loss: 0.9979 - hinge_accuracy: 0.5239"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 35/324 [==>...........................] - ETA: 54s - loss: 0.9981 - hinge_accuracy: 0.5205"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 36/324 [==>...........................] - ETA: 54s - loss: 0.9984 - hinge_accuracy: 0.5174"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 37/324 [==>...........................] - ETA: 54s - loss: 0.9980 - hinge_accuracy: 0.5194"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 38/324 [==>...........................] - ETA: 54s - loss: 0.9980 - hinge_accuracy: 0.5181"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 39/324 [==>...........................] - ETA: 53s - loss: 0.9980 - hinge_accuracy: 0.5168"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 40/324 [==>...........................] - ETA: 53s - loss: 0.9980 - hinge_accuracy: 0.5172"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 41/324 [==>...........................] - ETA: 53s - loss: 0.9982 - hinge_accuracy: 0.5160"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 42/324 [==>...........................] - ETA: 53s - loss: 0.9982 - hinge_accuracy: 0.5141"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 43/324 [==>...........................] - ETA: 53s - loss: 0.9982 - hinge_accuracy: 0.5160"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 44/324 [===>..........................] - ETA: 52s - loss: 0.9983 - hinge_accuracy: 0.5156"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 45/324 [===>..........................] - ETA: 52s - loss: 0.9990 - hinge_accuracy: 0.5104"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 46/324 [===>..........................] - ETA: 52s - loss: 0.9994 - hinge_accuracy: 0.5075"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 47/324 [===>..........................] - ETA: 52s - loss: 0.9992 - hinge_accuracy: 0.5093"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 48/324 [===>..........................] - ETA: 52s - loss: 0.9988 - hinge_accuracy: 0.5137"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 49/324 [===>..........................] - ETA: 51s - loss: 0.9989 - hinge_accuracy: 0.5128"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 50/324 [===>..........................] - ETA: 51s - loss: 0.9991 - hinge_accuracy: 0.5113"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 51/324 [===>..........................] - ETA: 51s - loss: 0.9993 - hinge_accuracy: 0.5086"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 52/324 [===>..........................] - ETA: 51s - loss: 0.9993 - hinge_accuracy: 0.5090"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 53/324 [===>..........................] - ETA: 51s - loss: 0.9995 - hinge_accuracy: 0.5071"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 54/324 [====>.........................] - ETA: 50s - loss: 0.9992 - hinge_accuracy: 0.5098"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 55/324 [====>.........................] - ETA: 50s - loss: 0.9991 - hinge_accuracy: 0.5108"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 56/324 [====>.........................] - ETA: 50s - loss: 0.9989 - hinge_accuracy: 0.5117"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 57/324 [====>.........................] - ETA: 50s - loss: 0.9990 - hinge_accuracy: 0.5115"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 58/324 [====>.........................] - ETA: 50s - loss: 0.9989 - hinge_accuracy: 0.5119"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 59/324 [====>.........................] - ETA: 49s - loss: 0.9989 - hinge_accuracy: 0.5122"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 60/324 [====>.........................] - ETA: 49s - loss: 0.9988 - hinge_accuracy: 0.5130"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 61/324 [====>.........................] - ETA: 49s - loss: 0.9989 - hinge_accuracy: 0.5118"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 62/324 [====>.........................] - ETA: 49s - loss: 0.9986 - hinge_accuracy: 0.5131"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 63/324 [====>.........................] - ETA: 49s - loss: 0.9985 - hinge_accuracy: 0.5134"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 64/324 [====>.........................] - ETA: 49s - loss: 0.9982 - hinge_accuracy: 0.5171"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 65/324 [=====>........................] - ETA: 48s - loss: 0.9983 - hinge_accuracy: 0.5168"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 66/324 [=====>........................] - ETA: 48s - loss: 0.9980 - hinge_accuracy: 0.5185"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 67/324 [=====>........................] - ETA: 48s - loss: 0.9978 - hinge_accuracy: 0.5201"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 68/324 [=====>........................] - ETA: 48s - loss: 0.9977 - hinge_accuracy: 0.5211"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 69/324 [=====>........................] - ETA: 48s - loss: 0.9977 - hinge_accuracy: 0.5213"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 70/324 [=====>........................] - ETA: 47s - loss: 0.9975 - hinge_accuracy: 0.5228"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 71/324 [=====>........................] - ETA: 47s - loss: 0.9975 - hinge_accuracy: 0.5229"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 72/324 [=====>........................] - ETA: 47s - loss: 0.9977 - hinge_accuracy: 0.5208"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 73/324 [=====>........................] - ETA: 47s - loss: 0.9979 - hinge_accuracy: 0.5197"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 74/324 [=====>........................] - ETA: 47s - loss: 0.9976 - hinge_accuracy: 0.5215"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 75/324 [=====>........................] - ETA: 46s - loss: 0.9977 - hinge_accuracy: 0.5217"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 76/324 [======>.......................] - ETA: 46s - loss: 0.9976 - hinge_accuracy: 0.5222"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 77/324 [======>.......................] - ETA: 46s - loss: 0.9974 - hinge_accuracy: 0.5227"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 78/324 [======>.......................] - ETA: 46s - loss: 0.9972 - hinge_accuracy: 0.5244"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 79/324 [======>.......................] - ETA: 46s - loss: 0.9971 - hinge_accuracy: 0.5249"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 80/324 [======>.......................] - ETA: 46s - loss: 0.9969 - hinge_accuracy: 0.5266"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 81/324 [======>.......................] - ETA: 45s - loss: 0.9966 - hinge_accuracy: 0.5289"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 82/324 [======>.......................] - ETA: 45s - loss: 0.9966 - hinge_accuracy: 0.5290"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 83/324 [======>.......................] - ETA: 45s - loss: 0.9966 - hinge_accuracy: 0.5290"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 84/324 [======>.......................] - ETA: 45s - loss: 0.9966 - hinge_accuracy: 0.5290"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 85/324 [======>.......................] - ETA: 45s - loss: 0.9965 - hinge_accuracy: 0.5298"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 86/324 [======>.......................] - ETA: 44s - loss: 0.9963 - hinge_accuracy: 0.5298"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 87/324 [=======>......................] - ETA: 44s - loss: 0.9966 - hinge_accuracy: 0.5269"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 88/324 [=======>......................] - ETA: 44s - loss: 0.9963 - hinge_accuracy: 0.5288"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 89/324 [=======>......................] - ETA: 44s - loss: 0.9962 - hinge_accuracy: 0.5288"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 90/324 [=======>......................] - ETA: 44s - loss: 0.9960 - hinge_accuracy: 0.5295"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 91/324 [=======>......................] - ETA: 43s - loss: 0.9959 - hinge_accuracy: 0.5295"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 92/324 [=======>......................] - ETA: 43s - loss: 0.9957 - hinge_accuracy: 0.5302"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 93/324 [=======>......................] - ETA: 43s - loss: 0.9954 - hinge_accuracy: 0.5316"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 94/324 [=======>......................] - ETA: 43s - loss: 0.9952 - hinge_accuracy: 0.5329"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 95/324 [=======>......................] - ETA: 43s - loss: 0.9951 - hinge_accuracy: 0.5329"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 96/324 [=======>......................] - ETA: 43s - loss: 0.9948 - hinge_accuracy: 0.5352"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 97/324 [=======>......................] - ETA: 42s - loss: 0.9948 - hinge_accuracy: 0.5345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 98/324 [========>.....................] - ETA: 42s - loss: 0.9951 - hinge_accuracy: 0.5322"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 99/324 [========>.....................] - ETA: 42s - loss: 0.9951 - hinge_accuracy: 0.5322"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "100/324 [========>.....................] - ETA: 42s - loss: 0.9949 - hinge_accuracy: 0.5325"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "101/324 [========>.....................] - ETA: 42s - loss: 0.9947 - hinge_accuracy: 0.5328"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "102/324 [========>.....................] - ETA: 41s - loss: 0.9943 - hinge_accuracy: 0.5337"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "103/324 [========>.....................] - ETA: 41s - loss: 0.9941 - hinge_accuracy: 0.5340"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "104/324 [========>.....................] - ETA: 41s - loss: 0.9940 - hinge_accuracy: 0.5343"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "105/324 [========>.....................] - ETA: 41s - loss: 0.9939 - hinge_accuracy: 0.5351"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "106/324 [========>.....................] - ETA: 41s - loss: 0.9937 - hinge_accuracy: 0.5357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "107/324 [========>.....................] - ETA: 40s - loss: 0.9935 - hinge_accuracy: 0.5359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "108/324 [=========>....................] - ETA: 40s - loss: 0.9938 - hinge_accuracy: 0.5350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "109/324 [=========>....................] - ETA: 40s - loss: 0.9938 - hinge_accuracy: 0.5344"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "110/324 [=========>....................] - ETA: 40s - loss: 0.9938 - hinge_accuracy: 0.5347"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "111/324 [=========>....................] - ETA: 40s - loss: 0.9937 - hinge_accuracy: 0.5338"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "112/324 [=========>....................] - ETA: 39s - loss: 0.9935 - hinge_accuracy: 0.5338"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "113/324 [=========>....................] - ETA: 39s - loss: 0.9933 - hinge_accuracy: 0.5337"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "114/324 [=========>....................] - ETA: 39s - loss: 0.9930 - hinge_accuracy: 0.5348"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "115/324 [=========>....................] - ETA: 39s - loss: 0.9928 - hinge_accuracy: 0.5353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "116/324 [=========>....................] - ETA: 39s - loss: 0.9930 - hinge_accuracy: 0.5339"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "117/324 [=========>....................] - ETA: 39s - loss: 0.9929 - hinge_accuracy: 0.5342"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "118/324 [=========>....................] - ETA: 38s - loss: 0.9926 - hinge_accuracy: 0.5344"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "119/324 [==========>...................] - ETA: 38s - loss: 0.9925 - hinge_accuracy: 0.5349"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "120/324 [==========>...................] - ETA: 38s - loss: 0.9922 - hinge_accuracy: 0.5357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "121/324 [==========>...................] - ETA: 38s - loss: 0.9921 - hinge_accuracy: 0.5359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "122/324 [==========>...................] - ETA: 38s - loss: 0.9923 - hinge_accuracy: 0.5343"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "123/324 [==========>...................] - ETA: 37s - loss: 0.9920 - hinge_accuracy: 0.5346"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "124/324 [==========>...................] - ETA: 37s - loss: 0.9921 - hinge_accuracy: 0.5330"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "125/324 [==========>...................] - ETA: 37s - loss: 0.9916 - hinge_accuracy: 0.5340"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "126/324 [==========>...................] - ETA: 37s - loss: 0.9914 - hinge_accuracy: 0.5345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "127/324 [==========>...................] - ETA: 37s - loss: 0.9910 - hinge_accuracy: 0.5349"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "128/324 [==========>...................] - ETA: 36s - loss: 0.9906 - hinge_accuracy: 0.5359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "129/324 [==========>...................] - ETA: 36s - loss: 0.9902 - hinge_accuracy: 0.5363"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "130/324 [===========>..................] - ETA: 36s - loss: 0.9901 - hinge_accuracy: 0.5365"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "131/324 [===========>..................] - ETA: 36s - loss: 0.9894 - hinge_accuracy: 0.5379"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "132/324 [===========>..................] - ETA: 36s - loss: 0.9895 - hinge_accuracy: 0.5369"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "133/324 [===========>..................] - ETA: 35s - loss: 0.9892 - hinge_accuracy: 0.5376"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "134/324 [===========>..................] - ETA: 35s - loss: 0.9888 - hinge_accuracy: 0.5385"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "135/324 [===========>..................] - ETA: 35s - loss: 0.9884 - hinge_accuracy: 0.5389"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "136/324 [===========>..................] - ETA: 35s - loss: 0.9881 - hinge_accuracy: 0.5398"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "137/324 [===========>..................] - ETA: 35s - loss: 0.9870 - hinge_accuracy: 0.5417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "138/324 [===========>..................] - ETA: 35s - loss: 0.9870 - hinge_accuracy: 0.5417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "139/324 [===========>..................] - ETA: 34s - loss: 0.9867 - hinge_accuracy: 0.5420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "140/324 [===========>..................] - ETA: 34s - loss: 0.9860 - hinge_accuracy: 0.5437"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "141/324 [============>.................] - ETA: 34s - loss: 0.9856 - hinge_accuracy: 0.5445"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "142/324 [============>.................] - ETA: 34s - loss: 0.9852 - hinge_accuracy: 0.5451"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "143/324 [============>.................] - ETA: 34s - loss: 0.9847 - hinge_accuracy: 0.5463"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "144/324 [============>.................] - ETA: 33s - loss: 0.9839 - hinge_accuracy: 0.5480"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "145/324 [============>.................] - ETA: 33s - loss: 0.9836 - hinge_accuracy: 0.5483"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "146/324 [============>.................] - ETA: 33s - loss: 0.9827 - hinge_accuracy: 0.5501"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "147/324 [============>.................] - ETA: 33s - loss: 0.9824 - hinge_accuracy: 0.5504"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "148/324 [============>.................] - ETA: 33s - loss: 0.9820 - hinge_accuracy: 0.5503"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "149/324 [============>.................] - ETA: 32s - loss: 0.9822 - hinge_accuracy: 0.5491"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "150/324 [============>.................] - ETA: 32s - loss: 0.9819 - hinge_accuracy: 0.5487"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "151/324 [============>.................] - ETA: 32s - loss: 0.9815 - hinge_accuracy: 0.5488"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "152/324 [=============>................] - ETA: 32s - loss: 0.9808 - hinge_accuracy: 0.5502"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "153/324 [=============>................] - ETA: 32s - loss: 0.9799 - hinge_accuracy: 0.5515"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "154/324 [=============>................] - ETA: 32s - loss: 0.9798 - hinge_accuracy: 0.5515"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "155/324 [=============>................] - ETA: 31s - loss: 0.9792 - hinge_accuracy: 0.5526"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "156/324 [=============>................] - ETA: 31s - loss: 0.9786 - hinge_accuracy: 0.5537"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "157/324 [=============>................] - ETA: 31s - loss: 0.9782 - hinge_accuracy: 0.5539"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "158/324 [=============>................] - ETA: 31s - loss: 0.9773 - hinge_accuracy: 0.5554"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "159/324 [=============>................] - ETA: 31s - loss: 0.9768 - hinge_accuracy: 0.5560"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "160/324 [=============>................] - ETA: 30s - loss: 0.9763 - hinge_accuracy: 0.5568"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "161/324 [=============>................] - ETA: 30s - loss: 0.9757 - hinge_accuracy: 0.5578"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "162/324 [==============>...............] - ETA: 30s - loss: 0.9751 - hinge_accuracy: 0.5586"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "163/324 [==============>...............] - ETA: 30s - loss: 0.9743 - hinge_accuracy: 0.5596"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "164/324 [==============>...............] - ETA: 30s - loss: 0.9738 - hinge_accuracy: 0.5602"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "165/324 [==============>...............] - ETA: 29s - loss: 0.9725 - hinge_accuracy: 0.5617"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "166/324 [==============>...............] - ETA: 29s - loss: 0.9726 - hinge_accuracy: 0.5614"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "167/324 [==============>...............] - ETA: 29s - loss: 0.9720 - hinge_accuracy: 0.5618"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "168/324 [==============>...............] - ETA: 29s - loss: 0.9707 - hinge_accuracy: 0.5631"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "169/324 [==============>...............] - ETA: 29s - loss: 0.9698 - hinge_accuracy: 0.5642"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "170/324 [==============>...............] - ETA: 28s - loss: 0.9694 - hinge_accuracy: 0.5645"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "171/324 [==============>...............] - ETA: 28s - loss: 0.9675 - hinge_accuracy: 0.5665"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "172/324 [==============>...............] - ETA: 28s - loss: 0.9669 - hinge_accuracy: 0.5670"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "173/324 [===============>..............] - ETA: 28s - loss: 0.9663 - hinge_accuracy: 0.5674"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "174/324 [===============>..............] - ETA: 28s - loss: 0.9652 - hinge_accuracy: 0.5688"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "175/324 [===============>..............] - ETA: 28s - loss: 0.9644 - hinge_accuracy: 0.5696"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "176/324 [===============>..............] - ETA: 27s - loss: 0.9638 - hinge_accuracy: 0.5703"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "177/324 [===============>..............] - ETA: 27s - loss: 0.9626 - hinge_accuracy: 0.5713"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "178/324 [===============>..............] - ETA: 27s - loss: 0.9613 - hinge_accuracy: 0.5723"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "179/324 [===============>..............] - ETA: 27s - loss: 0.9600 - hinge_accuracy: 0.5735"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "180/324 [===============>..............] - ETA: 27s - loss: 0.9597 - hinge_accuracy: 0.5738"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "181/324 [===============>..............] - ETA: 26s - loss: 0.9584 - hinge_accuracy: 0.5753"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "182/324 [===============>..............] - ETA: 26s - loss: 0.9579 - hinge_accuracy: 0.5759"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "183/324 [===============>..............] - ETA: 26s - loss: 0.9571 - hinge_accuracy: 0.5770"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "184/324 [================>.............] - ETA: 26s - loss: 0.9565 - hinge_accuracy: 0.5776"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "185/324 [================>.............] - ETA: 26s - loss: 0.9550 - hinge_accuracy: 0.5791"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "186/324 [================>.............] - ETA: 25s - loss: 0.9534 - hinge_accuracy: 0.5806"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "187/324 [================>.............] - ETA: 25s - loss: 0.9519 - hinge_accuracy: 0.5819"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "188/324 [================>.............] - ETA: 25s - loss: 0.9514 - hinge_accuracy: 0.5819"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "189/324 [================>.............] - ETA: 25s - loss: 0.9504 - hinge_accuracy: 0.5832"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "190/324 [================>.............] - ETA: 25s - loss: 0.9493 - hinge_accuracy: 0.5839"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "191/324 [================>.............] - ETA: 25s - loss: 0.9479 - hinge_accuracy: 0.5849"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "192/324 [================>.............] - ETA: 24s - loss: 0.9467 - hinge_accuracy: 0.5863"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "193/324 [================>.............] - ETA: 24s - loss: 0.9451 - hinge_accuracy: 0.5874"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "194/324 [================>.............] - ETA: 24s - loss: 0.9440 - hinge_accuracy: 0.5881"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "195/324 [=================>............] - ETA: 24s - loss: 0.9439 - hinge_accuracy: 0.5881"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "196/324 [=================>............] - ETA: 24s - loss: 0.9432 - hinge_accuracy: 0.5886"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "197/324 [=================>............] - ETA: 23s - loss: 0.9423 - hinge_accuracy: 0.5895"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "198/324 [=================>............] - ETA: 23s - loss: 0.9403 - hinge_accuracy: 0.5914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "199/324 [=================>............] - ETA: 23s - loss: 0.9399 - hinge_accuracy: 0.5919"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "200/324 [=================>............] - ETA: 23s - loss: 0.9390 - hinge_accuracy: 0.5930"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "201/324 [=================>............] - ETA: 23s - loss: 0.9379 - hinge_accuracy: 0.5939"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "202/324 [=================>............] - ETA: 22s - loss: 0.9368 - hinge_accuracy: 0.5947"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "203/324 [=================>............] - ETA: 22s - loss: 0.9363 - hinge_accuracy: 0.5950"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "204/324 [=================>............] - ETA: 22s - loss: 0.9350 - hinge_accuracy: 0.5957"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "205/324 [=================>............] - ETA: 22s - loss: 0.9341 - hinge_accuracy: 0.5960"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "206/324 [==================>...........] - ETA: 22s - loss: 0.9331 - hinge_accuracy: 0.5968"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "207/324 [==================>...........] - ETA: 22s - loss: 0.9318 - hinge_accuracy: 0.5978"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "208/324 [==================>...........] - ETA: 21s - loss: 0.9302 - hinge_accuracy: 0.5990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "209/324 [==================>...........] - ETA: 21s - loss: 0.9288 - hinge_accuracy: 0.6000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "210/324 [==================>...........] - ETA: 21s - loss: 0.9273 - hinge_accuracy: 0.6010"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "211/324 [==================>...........] - ETA: 21s - loss: 0.9258 - hinge_accuracy: 0.6019"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "212/324 [==================>...........] - ETA: 21s - loss: 0.9244 - hinge_accuracy: 0.6027"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "213/324 [==================>...........] - ETA: 20s - loss: 0.9235 - hinge_accuracy: 0.6033"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "214/324 [==================>...........] - ETA: 20s - loss: 0.9214 - hinge_accuracy: 0.6046"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "215/324 [==================>...........] - ETA: 20s - loss: 0.9197 - hinge_accuracy: 0.6055"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "216/324 [===================>..........] - ETA: 20s - loss: 0.9186 - hinge_accuracy: 0.6062"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "217/324 [===================>..........] - ETA: 20s - loss: 0.9169 - hinge_accuracy: 0.6073"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "218/324 [===================>..........] - ETA: 19s - loss: 0.9151 - hinge_accuracy: 0.6085"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "219/324 [===================>..........] - ETA: 19s - loss: 0.9137 - hinge_accuracy: 0.6094"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "220/324 [===================>..........] - ETA: 19s - loss: 0.9127 - hinge_accuracy: 0.6101"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "221/324 [===================>..........] - ETA: 19s - loss: 0.9112 - hinge_accuracy: 0.6109"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "222/324 [===================>..........] - ETA: 19s - loss: 0.9092 - hinge_accuracy: 0.6122"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "223/324 [===================>..........] - ETA: 19s - loss: 0.9075 - hinge_accuracy: 0.6132"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "224/324 [===================>..........] - ETA: 18s - loss: 0.9061 - hinge_accuracy: 0.6141"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "225/324 [===================>..........] - ETA: 18s - loss: 0.9043 - hinge_accuracy: 0.6150"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "226/324 [===================>..........] - ETA: 18s - loss: 0.9028 - hinge_accuracy: 0.6157"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "227/324 [====================>.........] - ETA: 18s - loss: 0.9016 - hinge_accuracy: 0.6166"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "228/324 [====================>.........] - ETA: 18s - loss: 0.9002 - hinge_accuracy: 0.6173"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "229/324 [====================>.........] - ETA: 17s - loss: 0.8982 - hinge_accuracy: 0.6184"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "230/324 [====================>.........] - ETA: 17s - loss: 0.8966 - hinge_accuracy: 0.6194"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "231/324 [====================>.........] - ETA: 17s - loss: 0.8964 - hinge_accuracy: 0.6195"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "232/324 [====================>.........] - ETA: 17s - loss: 0.8946 - hinge_accuracy: 0.6206"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "233/324 [====================>.........] - ETA: 17s - loss: 0.8939 - hinge_accuracy: 0.6208"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "234/324 [====================>.........] - ETA: 16s - loss: 0.8926 - hinge_accuracy: 0.6215"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "235/324 [====================>.........] - ETA: 16s - loss: 0.8908 - hinge_accuracy: 0.6225"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "236/324 [====================>.........] - ETA: 16s - loss: 0.8903 - hinge_accuracy: 0.6226"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "237/324 [====================>.........] - ETA: 16s - loss: 0.8885 - hinge_accuracy: 0.6235"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "238/324 [=====================>........] - ETA: 16s - loss: 0.8874 - hinge_accuracy: 0.6239"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "239/324 [=====================>........] - ETA: 15s - loss: 0.8868 - hinge_accuracy: 0.6242"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "240/324 [=====================>........] - ETA: 15s - loss: 0.8853 - hinge_accuracy: 0.6249"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "241/324 [=====================>........] - ETA: 15s - loss: 0.8842 - hinge_accuracy: 0.6253"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "242/324 [=====================>........] - ETA: 15s - loss: 0.8824 - hinge_accuracy: 0.6262"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "243/324 [=====================>........] - ETA: 15s - loss: 0.8814 - hinge_accuracy: 0.6264"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "244/324 [=====================>........] - ETA: 15s - loss: 0.8800 - hinge_accuracy: 0.6272"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "245/324 [=====================>........] - ETA: 14s - loss: 0.8793 - hinge_accuracy: 0.6276"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "246/324 [=====================>........] - ETA: 14s - loss: 0.8780 - hinge_accuracy: 0.6282"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "247/324 [=====================>........] - ETA: 14s - loss: 0.8773 - hinge_accuracy: 0.6283"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "248/324 [=====================>........] - ETA: 14s - loss: 0.8766 - hinge_accuracy: 0.6285"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "249/324 [======================>.......] - ETA: 14s - loss: 0.8749 - hinge_accuracy: 0.6293"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "250/324 [======================>.......] - ETA: 13s - loss: 0.8739 - hinge_accuracy: 0.6295"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "251/324 [======================>.......] - ETA: 13s - loss: 0.8727 - hinge_accuracy: 0.6301"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "252/324 [======================>.......] - ETA: 13s - loss: 0.8715 - hinge_accuracy: 0.6307"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "253/324 [======================>.......] - ETA: 13s - loss: 0.8704 - hinge_accuracy: 0.6311"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "254/324 [======================>.......] - ETA: 13s - loss: 0.8703 - hinge_accuracy: 0.6308"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "255/324 [======================>.......] - ETA: 12s - loss: 0.8689 - hinge_accuracy: 0.6314"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "256/324 [======================>.......] - ETA: 12s - loss: 0.8670 - hinge_accuracy: 0.6323"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "257/324 [======================>.......] - ETA: 12s - loss: 0.8652 - hinge_accuracy: 0.6334"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "258/324 [======================>.......] - ETA: 12s - loss: 0.8635 - hinge_accuracy: 0.6344"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "259/324 [======================>.......] - ETA: 12s - loss: 0.8619 - hinge_accuracy: 0.6353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "260/324 [=======================>......] - ETA: 12s - loss: 0.8604 - hinge_accuracy: 0.6361"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "261/324 [=======================>......] - ETA: 11s - loss: 0.8596 - hinge_accuracy: 0.6365"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "262/324 [=======================>......] - ETA: 11s - loss: 0.8582 - hinge_accuracy: 0.6372"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "263/324 [=======================>......] - ETA: 11s - loss: 0.8565 - hinge_accuracy: 0.6380"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "264/324 [=======================>......] - ETA: 11s - loss: 0.8551 - hinge_accuracy: 0.6386"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "265/324 [=======================>......] - ETA: 11s - loss: 0.8540 - hinge_accuracy: 0.6389"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "266/324 [=======================>......] - ETA: 10s - loss: 0.8521 - hinge_accuracy: 0.6399"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "267/324 [=======================>......] - ETA: 10s - loss: 0.8506 - hinge_accuracy: 0.6407"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "268/324 [=======================>......] - ETA: 10s - loss: 0.8493 - hinge_accuracy: 0.6413"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "269/324 [=======================>......] - ETA: 10s - loss: 0.8482 - hinge_accuracy: 0.6420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "270/324 [========================>.....] - ETA: 10s - loss: 0.8477 - hinge_accuracy: 0.6420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "271/324 [========================>.....] - ETA: 9s - loss: 0.8466 - hinge_accuracy: 0.6426 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "272/324 [========================>.....] - ETA: 9s - loss: 0.8457 - hinge_accuracy: 0.6429"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "273/324 [========================>.....] - ETA: 9s - loss: 0.8448 - hinge_accuracy: 0.6432"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "274/324 [========================>.....] - ETA: 9s - loss: 0.8439 - hinge_accuracy: 0.6437"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "275/324 [========================>.....] - ETA: 9s - loss: 0.8434 - hinge_accuracy: 0.6439"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "276/324 [========================>.....] - ETA: 9s - loss: 0.8422 - hinge_accuracy: 0.6445"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "277/324 [========================>.....] - ETA: 8s - loss: 0.8408 - hinge_accuracy: 0.6453"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "278/324 [========================>.....] - ETA: 8s - loss: 0.8395 - hinge_accuracy: 0.6460"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "279/324 [========================>.....] - ETA: 8s - loss: 0.8384 - hinge_accuracy: 0.6464"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "280/324 [========================>.....] - ETA: 8s - loss: 0.8365 - hinge_accuracy: 0.6473"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "281/324 [=========================>....] - ETA: 8s - loss: 0.8346 - hinge_accuracy: 0.6482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "282/324 [=========================>....] - ETA: 7s - loss: 0.8328 - hinge_accuracy: 0.6490"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "283/324 [=========================>....] - ETA: 7s - loss: 0.8319 - hinge_accuracy: 0.6494"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "284/324 [=========================>....] - ETA: 7s - loss: 0.8311 - hinge_accuracy: 0.6498"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "285/324 [=========================>....] - ETA: 7s - loss: 0.8297 - hinge_accuracy: 0.6504"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "286/324 [=========================>....] - ETA: 7s - loss: 0.8281 - hinge_accuracy: 0.6511"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "287/324 [=========================>....] - ETA: 6s - loss: 0.8276 - hinge_accuracy: 0.6514"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "288/324 [=========================>....] - ETA: 6s - loss: 0.8262 - hinge_accuracy: 0.6520"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "289/324 [=========================>....] - ETA: 6s - loss: 0.8251 - hinge_accuracy: 0.6526"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "290/324 [=========================>....] - ETA: 6s - loss: 0.8238 - hinge_accuracy: 0.6533"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "291/324 [=========================>....] - ETA: 6s - loss: 0.8232 - hinge_accuracy: 0.6537"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "292/324 [==========================>...] - ETA: 6s - loss: 0.8219 - hinge_accuracy: 0.6542"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "293/324 [==========================>...] - ETA: 5s - loss: 0.8206 - hinge_accuracy: 0.6550"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "294/324 [==========================>...] - ETA: 5s - loss: 0.8190 - hinge_accuracy: 0.6558"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "295/324 [==========================>...] - ETA: 5s - loss: 0.8177 - hinge_accuracy: 0.6566"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "296/324 [==========================>...] - ETA: 5s - loss: 0.8161 - hinge_accuracy: 0.6573"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "297/324 [==========================>...] - ETA: 5s - loss: 0.8156 - hinge_accuracy: 0.6576"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "298/324 [==========================>...] - ETA: 4s - loss: 0.8146 - hinge_accuracy: 0.6580"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "299/324 [==========================>...] - ETA: 4s - loss: 0.8136 - hinge_accuracy: 0.6585"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "300/324 [==========================>...] - ETA: 4s - loss: 0.8123 - hinge_accuracy: 0.6593"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "301/324 [==========================>...] - ETA: 4s - loss: 0.8115 - hinge_accuracy: 0.6598"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "302/324 [==========================>...] - ETA: 4s - loss: 0.8112 - hinge_accuracy: 0.6599"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "303/324 [===========================>..] - ETA: 3s - loss: 0.8099 - hinge_accuracy: 0.6606"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "304/324 [===========================>..] - ETA: 3s - loss: 0.8082 - hinge_accuracy: 0.6615"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "305/324 [===========================>..] - ETA: 3s - loss: 0.8069 - hinge_accuracy: 0.6622"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "306/324 [===========================>..] - ETA: 3s - loss: 0.8056 - hinge_accuracy: 0.6630"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "307/324 [===========================>..] - ETA: 3s - loss: 0.8045 - hinge_accuracy: 0.6636"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "308/324 [===========================>..] - ETA: 3s - loss: 0.8030 - hinge_accuracy: 0.6644"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "309/324 [===========================>..] - ETA: 2s - loss: 0.8024 - hinge_accuracy: 0.6647"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "310/324 [===========================>..] - ETA: 2s - loss: 0.8013 - hinge_accuracy: 0.6654"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "311/324 [===========================>..] - ETA: 2s - loss: 0.8001 - hinge_accuracy: 0.6660"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "312/324 [===========================>..] - ETA: 2s - loss: 0.7985 - hinge_accuracy: 0.6668"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "313/324 [===========================>..] - ETA: 2s - loss: 0.7972 - hinge_accuracy: 0.6674"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "314/324 [============================>.] - ETA: 1s - loss: 0.7958 - hinge_accuracy: 0.6683"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "315/324 [============================>.] - ETA: 1s - loss: 0.7942 - hinge_accuracy: 0.6691"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "316/324 [============================>.] - ETA: 1s - loss: 0.7930 - hinge_accuracy: 0.6697"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "317/324 [============================>.] - ETA: 1s - loss: 0.7919 - hinge_accuracy: 0.6701"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "318/324 [============================>.] - ETA: 1s - loss: 0.7906 - hinge_accuracy: 0.6708"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "319/324 [============================>.] - ETA: 0s - loss: 0.7896 - hinge_accuracy: 0.6712"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "320/324 [============================>.] - ETA: 0s - loss: 0.7889 - hinge_accuracy: 0.6717"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "321/324 [============================>.] - ETA: 0s - loss: 0.7877 - hinge_accuracy: 0.6722"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "322/324 [============================>.] - ETA: 0s - loss: 0.7869 - hinge_accuracy: 0.6727"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "323/324 [============================>.] - ETA: 0s - loss: 0.7856 - hinge_accuracy: 0.6735"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - ETA: 0s - loss: 0.7855 - hinge_accuracy: 0.6745"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - 64s 196ms/step - loss: 0.7855 - hinge_accuracy: 0.6745 - val_loss: 0.5021 - val_hinge_accuracy: 0.8080\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 2/3\n",
      "\r",
      "  1/324 [..............................] - ETA: 1:00 - loss: 0.5268 - hinge_accuracy: 0.8125"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  2/324 [..............................] - ETA: 59s - loss: 0.4840 - hinge_accuracy: 0.8281 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  3/324 [..............................] - ETA: 1:00 - loss: 0.4671 - hinge_accuracy: 0.8333"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  4/324 [..............................] - ETA: 1:00 - loss: 0.4689 - hinge_accuracy: 0.8281"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  5/324 [..............................] - ETA: 59s - loss: 0.4641 - hinge_accuracy: 0.8250 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  6/324 [..............................] - ETA: 59s - loss: 0.4790 - hinge_accuracy: 0.8177"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  7/324 [..............................] - ETA: 59s - loss: 0.4643 - hinge_accuracy: 0.8259"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  8/324 [..............................] - ETA: 59s - loss: 0.4585 - hinge_accuracy: 0.8281"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  9/324 [..............................] - ETA: 59s - loss: 0.4598 - hinge_accuracy: 0.8264"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 10/324 [..............................] - ETA: 59s - loss: 0.4566 - hinge_accuracy: 0.8313"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 11/324 [>.............................] - ETA: 58s - loss: 0.4440 - hinge_accuracy: 0.8352"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 12/324 [>.............................] - ETA: 58s - loss: 0.4467 - hinge_accuracy: 0.8333"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 13/324 [>.............................] - ETA: 58s - loss: 0.4464 - hinge_accuracy: 0.8341"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 14/324 [>.............................] - ETA: 58s - loss: 0.4359 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 15/324 [>.............................] - ETA: 58s - loss: 0.4335 - hinge_accuracy: 0.8438"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 16/324 [>.............................] - ETA: 58s - loss: 0.4222 - hinge_accuracy: 0.8496"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 17/324 [>.............................] - ETA: 57s - loss: 0.4193 - hinge_accuracy: 0.8548"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 18/324 [>.............................] - ETA: 57s - loss: 0.4257 - hinge_accuracy: 0.8507"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 19/324 [>.............................] - ETA: 57s - loss: 0.4313 - hinge_accuracy: 0.8487"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 20/324 [>.............................] - ETA: 57s - loss: 0.4360 - hinge_accuracy: 0.8469"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 21/324 [>.............................] - ETA: 57s - loss: 0.4343 - hinge_accuracy: 0.8482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 22/324 [=>............................] - ETA: 56s - loss: 0.4370 - hinge_accuracy: 0.8466"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 23/324 [=>............................] - ETA: 56s - loss: 0.4413 - hinge_accuracy: 0.8451"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 24/324 [=>............................] - ETA: 56s - loss: 0.4366 - hinge_accuracy: 0.8464"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 25/324 [=>............................] - ETA: 56s - loss: 0.4311 - hinge_accuracy: 0.8500"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 26/324 [=>............................] - ETA: 56s - loss: 0.4331 - hinge_accuracy: 0.8486"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 27/324 [=>............................] - ETA: 55s - loss: 0.4292 - hinge_accuracy: 0.8495"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 28/324 [=>............................] - ETA: 55s - loss: 0.4316 - hinge_accuracy: 0.8482"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 29/324 [=>............................] - ETA: 55s - loss: 0.4271 - hinge_accuracy: 0.8502"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 30/324 [=>............................] - ETA: 55s - loss: 0.4335 - hinge_accuracy: 0.8469"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 31/324 [=>............................] - ETA: 55s - loss: 0.4342 - hinge_accuracy: 0.8468"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 32/324 [=>............................] - ETA: 54s - loss: 0.4335 - hinge_accuracy: 0.8477"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 33/324 [==>...........................] - ETA: 54s - loss: 0.4288 - hinge_accuracy: 0.8504"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 34/324 [==>...........................] - ETA: 54s - loss: 0.4270 - hinge_accuracy: 0.8511"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 35/324 [==>...........................] - ETA: 54s - loss: 0.4240 - hinge_accuracy: 0.8527"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 36/324 [==>...........................] - ETA: 54s - loss: 0.4234 - hinge_accuracy: 0.8516"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 37/324 [==>...........................] - ETA: 53s - loss: 0.4210 - hinge_accuracy: 0.8530"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 38/324 [==>...........................] - ETA: 53s - loss: 0.4177 - hinge_accuracy: 0.8544"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 39/324 [==>...........................] - ETA: 53s - loss: 0.4199 - hinge_accuracy: 0.8542"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 40/324 [==>...........................] - ETA: 53s - loss: 0.4198 - hinge_accuracy: 0.8539"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 41/324 [==>...........................] - ETA: 53s - loss: 0.4271 - hinge_accuracy: 0.8498"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 42/324 [==>...........................] - ETA: 52s - loss: 0.4260 - hinge_accuracy: 0.8497"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 43/324 [==>...........................] - ETA: 52s - loss: 0.4230 - hinge_accuracy: 0.8510"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 44/324 [===>..........................] - ETA: 52s - loss: 0.4191 - hinge_accuracy: 0.8530"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 45/324 [===>..........................] - ETA: 52s - loss: 0.4171 - hinge_accuracy: 0.8535"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 46/324 [===>..........................] - ETA: 52s - loss: 0.4216 - hinge_accuracy: 0.8505"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 47/324 [===>..........................] - ETA: 52s - loss: 0.4254 - hinge_accuracy: 0.8477"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 48/324 [===>..........................] - ETA: 51s - loss: 0.4308 - hinge_accuracy: 0.8438"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 49/324 [===>..........................] - ETA: 51s - loss: 0.4293 - hinge_accuracy: 0.8438"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 50/324 [===>..........................] - ETA: 51s - loss: 0.4279 - hinge_accuracy: 0.8444"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 51/324 [===>..........................] - ETA: 51s - loss: 0.4269 - hinge_accuracy: 0.8450"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 52/324 [===>..........................] - ETA: 51s - loss: 0.4272 - hinge_accuracy: 0.8444"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 53/324 [===>..........................] - ETA: 50s - loss: 0.4292 - hinge_accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 54/324 [====>.........................] - ETA: 50s - loss: 0.4282 - hinge_accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 55/324 [====>.........................] - ETA: 50s - loss: 0.4301 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 56/324 [====>.........................] - ETA: 50s - loss: 0.4303 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 57/324 [====>.........................] - ETA: 50s - loss: 0.4320 - hinge_accuracy: 0.8399"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 58/324 [====>.........................] - ETA: 49s - loss: 0.4311 - hinge_accuracy: 0.8400"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 59/324 [====>.........................] - ETA: 49s - loss: 0.4278 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 60/324 [====>.........................] - ETA: 49s - loss: 0.4279 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 61/324 [====>.........................] - ETA: 49s - loss: 0.4287 - hinge_accuracy: 0.8407"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 62/324 [====>.........................] - ETA: 49s - loss: 0.4283 - hinge_accuracy: 0.8407"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 63/324 [====>.........................] - ETA: 49s - loss: 0.4273 - hinge_accuracy: 0.8413"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 64/324 [====>.........................] - ETA: 48s - loss: 0.4257 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 65/324 [=====>........................] - ETA: 48s - loss: 0.4249 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 66/324 [=====>........................] - ETA: 48s - loss: 0.4243 - hinge_accuracy: 0.8428"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 67/324 [=====>........................] - ETA: 48s - loss: 0.4255 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 68/324 [=====>........................] - ETA: 48s - loss: 0.4248 - hinge_accuracy: 0.8424"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 69/324 [=====>........................] - ETA: 47s - loss: 0.4220 - hinge_accuracy: 0.8438"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 70/324 [=====>........................] - ETA: 47s - loss: 0.4230 - hinge_accuracy: 0.8433"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 71/324 [=====>........................] - ETA: 47s - loss: 0.4222 - hinge_accuracy: 0.8442"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 72/324 [=====>........................] - ETA: 47s - loss: 0.4241 - hinge_accuracy: 0.8429"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 73/324 [=====>........................] - ETA: 47s - loss: 0.4245 - hinge_accuracy: 0.8425"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 74/324 [=====>........................] - ETA: 46s - loss: 0.4219 - hinge_accuracy: 0.8442"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 75/324 [=====>........................] - ETA: 46s - loss: 0.4246 - hinge_accuracy: 0.8425"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 76/324 [======>.......................] - ETA: 46s - loss: 0.4250 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 77/324 [======>.......................] - ETA: 46s - loss: 0.4253 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 78/324 [======>.......................] - ETA: 46s - loss: 0.4251 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 79/324 [======>.......................] - ETA: 46s - loss: 0.4239 - hinge_accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 80/324 [======>.......................] - ETA: 45s - loss: 0.4249 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 81/324 [======>.......................] - ETA: 45s - loss: 0.4239 - hinge_accuracy: 0.8426"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 82/324 [======>.......................] - ETA: 45s - loss: 0.4252 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 83/324 [======>.......................] - ETA: 45s - loss: 0.4256 - hinge_accuracy: 0.8411"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 84/324 [======>.......................] - ETA: 45s - loss: 0.4266 - hinge_accuracy: 0.8400"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 85/324 [======>.......................] - ETA: 44s - loss: 0.4279 - hinge_accuracy: 0.8393"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 86/324 [======>.......................] - ETA: 44s - loss: 0.4287 - hinge_accuracy: 0.8387"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 87/324 [=======>......................] - ETA: 44s - loss: 0.4282 - hinge_accuracy: 0.8394"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 88/324 [=======>......................] - ETA: 44s - loss: 0.4272 - hinge_accuracy: 0.8398"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 89/324 [=======>......................] - ETA: 44s - loss: 0.4275 - hinge_accuracy: 0.8395"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 90/324 [=======>......................] - ETA: 43s - loss: 0.4292 - hinge_accuracy: 0.8382"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 91/324 [=======>......................] - ETA: 43s - loss: 0.4301 - hinge_accuracy: 0.8372"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 92/324 [=======>......................] - ETA: 43s - loss: 0.4289 - hinge_accuracy: 0.8380"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 93/324 [=======>......................] - ETA: 43s - loss: 0.4307 - hinge_accuracy: 0.8367"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 94/324 [=======>......................] - ETA: 43s - loss: 0.4319 - hinge_accuracy: 0.8358"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 95/324 [=======>......................] - ETA: 43s - loss: 0.4316 - hinge_accuracy: 0.8359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 96/324 [=======>......................] - ETA: 42s - loss: 0.4314 - hinge_accuracy: 0.8356"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 97/324 [=======>......................] - ETA: 42s - loss: 0.4322 - hinge_accuracy: 0.8347"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 98/324 [========>.....................] - ETA: 42s - loss: 0.4316 - hinge_accuracy: 0.8348"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 99/324 [========>.....................] - ETA: 42s - loss: 0.4298 - hinge_accuracy: 0.8355"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "100/324 [========>.....................] - ETA: 42s - loss: 0.4305 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "101/324 [========>.....................] - ETA: 41s - loss: 0.4292 - hinge_accuracy: 0.8357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "102/324 [========>.....................] - ETA: 41s - loss: 0.4299 - hinge_accuracy: 0.8355"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "103/324 [========>.....................] - ETA: 41s - loss: 0.4282 - hinge_accuracy: 0.8362"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "104/324 [========>.....................] - ETA: 41s - loss: 0.4281 - hinge_accuracy: 0.8356"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "105/324 [========>.....................] - ETA: 41s - loss: 0.4282 - hinge_accuracy: 0.8351"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "106/324 [========>.....................] - ETA: 40s - loss: 0.4302 - hinge_accuracy: 0.8337"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "107/324 [========>.....................] - ETA: 40s - loss: 0.4300 - hinge_accuracy: 0.8335"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "108/324 [=========>....................] - ETA: 40s - loss: 0.4293 - hinge_accuracy: 0.8342"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "109/324 [=========>....................] - ETA: 40s - loss: 0.4287 - hinge_accuracy: 0.8343"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "110/324 [=========>....................] - ETA: 40s - loss: 0.4285 - hinge_accuracy: 0.8344"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "111/324 [=========>....................] - ETA: 40s - loss: 0.4280 - hinge_accuracy: 0.8345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "112/324 [=========>....................] - ETA: 39s - loss: 0.4257 - hinge_accuracy: 0.8357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "113/324 [=========>....................] - ETA: 39s - loss: 0.4254 - hinge_accuracy: 0.8357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "114/324 [=========>....................] - ETA: 39s - loss: 0.4269 - hinge_accuracy: 0.8347"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "115/324 [=========>....................] - ETA: 39s - loss: 0.4269 - hinge_accuracy: 0.8345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "116/324 [=========>....................] - ETA: 39s - loss: 0.4259 - hinge_accuracy: 0.8349"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "117/324 [=========>....................] - ETA: 38s - loss: 0.4257 - hinge_accuracy: 0.8347"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "118/324 [=========>....................] - ETA: 38s - loss: 0.4254 - hinge_accuracy: 0.8347"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "119/324 [==========>...................] - ETA: 38s - loss: 0.4260 - hinge_accuracy: 0.8343"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "120/324 [==========>...................] - ETA: 38s - loss: 0.4251 - hinge_accuracy: 0.8346"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "121/324 [==========>...................] - ETA: 38s - loss: 0.4254 - hinge_accuracy: 0.8345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "122/324 [==========>...................] - ETA: 37s - loss: 0.4258 - hinge_accuracy: 0.8338"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "123/324 [==========>...................] - ETA: 37s - loss: 0.4263 - hinge_accuracy: 0.8336"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "124/324 [==========>...................] - ETA: 37s - loss: 0.4251 - hinge_accuracy: 0.8342"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "125/324 [==========>...................] - ETA: 37s - loss: 0.4253 - hinge_accuracy: 0.8340"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "126/324 [==========>...................] - ETA: 37s - loss: 0.4249 - hinge_accuracy: 0.8341"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "127/324 [==========>...................] - ETA: 37s - loss: 0.4239 - hinge_accuracy: 0.8346"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "128/324 [==========>...................] - ETA: 36s - loss: 0.4236 - hinge_accuracy: 0.8345"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "129/324 [==========>...................] - ETA: 36s - loss: 0.4249 - hinge_accuracy: 0.8333"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "130/324 [===========>..................] - ETA: 36s - loss: 0.4264 - hinge_accuracy: 0.8320"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "131/324 [===========>..................] - ETA: 36s - loss: 0.4258 - hinge_accuracy: 0.8321"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "132/324 [===========>..................] - ETA: 36s - loss: 0.4258 - hinge_accuracy: 0.8319"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "133/324 [===========>..................] - ETA: 35s - loss: 0.4250 - hinge_accuracy: 0.8322"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "134/324 [===========>..................] - ETA: 35s - loss: 0.4239 - hinge_accuracy: 0.8326"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "135/324 [===========>..................] - ETA: 35s - loss: 0.4227 - hinge_accuracy: 0.8326"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "136/324 [===========>..................] - ETA: 35s - loss: 0.4224 - hinge_accuracy: 0.8323"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "137/324 [===========>..................] - ETA: 35s - loss: 0.4228 - hinge_accuracy: 0.8323"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "138/324 [===========>..................] - ETA: 34s - loss: 0.4219 - hinge_accuracy: 0.8329"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "139/324 [===========>..................] - ETA: 34s - loss: 0.4216 - hinge_accuracy: 0.8327"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "140/324 [===========>..................] - ETA: 34s - loss: 0.4212 - hinge_accuracy: 0.8328"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "141/324 [============>.................] - ETA: 34s - loss: 0.4212 - hinge_accuracy: 0.8327"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "142/324 [============>.................] - ETA: 34s - loss: 0.4208 - hinge_accuracy: 0.8327"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "143/324 [============>.................] - ETA: 34s - loss: 0.4217 - hinge_accuracy: 0.8324"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "144/324 [============>.................] - ETA: 33s - loss: 0.4221 - hinge_accuracy: 0.8320"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "145/324 [============>.................] - ETA: 33s - loss: 0.4224 - hinge_accuracy: 0.8315"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "146/324 [============>.................] - ETA: 33s - loss: 0.4215 - hinge_accuracy: 0.8324"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "147/324 [============>.................] - ETA: 33s - loss: 0.4213 - hinge_accuracy: 0.8327"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "148/324 [============>.................] - ETA: 33s - loss: 0.4210 - hinge_accuracy: 0.8328"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "149/324 [============>.................] - ETA: 32s - loss: 0.4219 - hinge_accuracy: 0.8324"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "150/324 [============>.................] - ETA: 32s - loss: 0.4211 - hinge_accuracy: 0.8329"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "151/324 [============>.................] - ETA: 32s - loss: 0.4200 - hinge_accuracy: 0.8334"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "152/324 [=============>................] - ETA: 32s - loss: 0.4192 - hinge_accuracy: 0.8339"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "153/324 [=============>................] - ETA: 32s - loss: 0.4189 - hinge_accuracy: 0.8342"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "154/324 [=============>................] - ETA: 31s - loss: 0.4181 - hinge_accuracy: 0.8346"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "155/324 [=============>................] - ETA: 31s - loss: 0.4173 - hinge_accuracy: 0.8349"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "156/324 [=============>................] - ETA: 31s - loss: 0.4166 - hinge_accuracy: 0.8357"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "157/324 [=============>................] - ETA: 31s - loss: 0.4164 - hinge_accuracy: 0.8356"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "158/324 [=============>................] - ETA: 31s - loss: 0.4163 - hinge_accuracy: 0.8354"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "159/324 [=============>................] - ETA: 30s - loss: 0.4164 - hinge_accuracy: 0.8351"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "160/324 [=============>................] - ETA: 30s - loss: 0.4162 - hinge_accuracy: 0.8348"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "161/324 [=============>................] - ETA: 30s - loss: 0.4159 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "162/324 [==============>...............] - ETA: 30s - loss: 0.4155 - hinge_accuracy: 0.8355"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "163/324 [==============>...............] - ETA: 30s - loss: 0.4155 - hinge_accuracy: 0.8353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "164/324 [==============>...............] - ETA: 30s - loss: 0.4156 - hinge_accuracy: 0.8352"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "165/324 [==============>...............] - ETA: 29s - loss: 0.4153 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "166/324 [==============>...............] - ETA: 29s - loss: 0.4146 - hinge_accuracy: 0.8353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "167/324 [==============>...............] - ETA: 29s - loss: 0.4152 - hinge_accuracy: 0.8353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "168/324 [==============>...............] - ETA: 29s - loss: 0.4159 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "169/324 [==============>...............] - ETA: 29s - loss: 0.4162 - hinge_accuracy: 0.8349"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "170/324 [==============>...............] - ETA: 28s - loss: 0.4161 - hinge_accuracy: 0.8351"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "171/324 [==============>...............] - ETA: 28s - loss: 0.4167 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "172/324 [==============>...............] - ETA: 28s - loss: 0.4165 - hinge_accuracy: 0.8350"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "173/324 [===============>..............] - ETA: 28s - loss: 0.4173 - hinge_accuracy: 0.8344"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "174/324 [===============>..............] - ETA: 28s - loss: 0.4167 - hinge_accuracy: 0.8348"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "175/324 [===============>..............] - ETA: 27s - loss: 0.4164 - hinge_accuracy: 0.8348"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "176/324 [===============>..............] - ETA: 27s - loss: 0.4155 - hinge_accuracy: 0.8354"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "177/324 [===============>..............] - ETA: 27s - loss: 0.4153 - hinge_accuracy: 0.8353"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "178/324 [===============>..............] - ETA: 27s - loss: 0.4154 - hinge_accuracy: 0.8351"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "179/324 [===============>..............] - ETA: 27s - loss: 0.4151 - hinge_accuracy: 0.8354"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "180/324 [===============>..............] - ETA: 27s - loss: 0.4138 - hinge_accuracy: 0.8359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "181/324 [===============>..............] - ETA: 26s - loss: 0.4134 - hinge_accuracy: 0.8363"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "182/324 [===============>..............] - ETA: 26s - loss: 0.4134 - hinge_accuracy: 0.8362"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "183/324 [===============>..............] - ETA: 26s - loss: 0.4137 - hinge_accuracy: 0.8359"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "184/324 [================>.............] - ETA: 26s - loss: 0.4140 - hinge_accuracy: 0.8356"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "185/324 [================>.............] - ETA: 26s - loss: 0.4136 - hinge_accuracy: 0.8358"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "186/324 [================>.............] - ETA: 25s - loss: 0.4132 - hinge_accuracy: 0.8360"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "187/324 [================>.............] - ETA: 25s - loss: 0.4128 - hinge_accuracy: 0.8361"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "188/324 [================>.............] - ETA: 25s - loss: 0.4120 - hinge_accuracy: 0.8366"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "189/324 [================>.............] - ETA: 25s - loss: 0.4117 - hinge_accuracy: 0.8370"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "190/324 [================>.............] - ETA: 25s - loss: 0.4114 - hinge_accuracy: 0.8370"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "191/324 [================>.............] - ETA: 24s - loss: 0.4111 - hinge_accuracy: 0.8370"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "192/324 [================>.............] - ETA: 24s - loss: 0.4114 - hinge_accuracy: 0.8368"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "193/324 [================>.............] - ETA: 24s - loss: 0.4108 - hinge_accuracy: 0.8371"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "194/324 [================>.............] - ETA: 24s - loss: 0.4106 - hinge_accuracy: 0.8371"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "195/324 [=================>............] - ETA: 24s - loss: 0.4100 - hinge_accuracy: 0.8375"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "196/324 [=================>............] - ETA: 24s - loss: 0.4104 - hinge_accuracy: 0.8372"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "197/324 [=================>............] - ETA: 23s - loss: 0.4096 - hinge_accuracy: 0.8374"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "198/324 [=================>............] - ETA: 23s - loss: 0.4090 - hinge_accuracy: 0.8376"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "199/324 [=================>............] - ETA: 23s - loss: 0.4086 - hinge_accuracy: 0.8379"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "200/324 [=================>............] - ETA: 23s - loss: 0.4090 - hinge_accuracy: 0.8381"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "201/324 [=================>............] - ETA: 23s - loss: 0.4086 - hinge_accuracy: 0.8385"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "202/324 [=================>............] - ETA: 22s - loss: 0.4085 - hinge_accuracy: 0.8383"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "203/324 [=================>............] - ETA: 22s - loss: 0.4081 - hinge_accuracy: 0.8385"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "204/324 [=================>............] - ETA: 22s - loss: 0.4084 - hinge_accuracy: 0.8385"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "205/324 [=================>............] - ETA: 22s - loss: 0.4079 - hinge_accuracy: 0.8389"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "206/324 [==================>...........] - ETA: 22s - loss: 0.4079 - hinge_accuracy: 0.8387"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "207/324 [==================>...........] - ETA: 21s - loss: 0.4082 - hinge_accuracy: 0.8385"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "208/324 [==================>...........] - ETA: 21s - loss: 0.4076 - hinge_accuracy: 0.8391"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "209/324 [==================>...........] - ETA: 21s - loss: 0.4086 - hinge_accuracy: 0.8387"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "210/324 [==================>...........] - ETA: 21s - loss: 0.4084 - hinge_accuracy: 0.8387"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "211/324 [==================>...........] - ETA: 21s - loss: 0.4082 - hinge_accuracy: 0.8390"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "212/324 [==================>...........] - ETA: 21s - loss: 0.4077 - hinge_accuracy: 0.8393"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "213/324 [==================>...........] - ETA: 20s - loss: 0.4074 - hinge_accuracy: 0.8396"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "214/324 [==================>...........] - ETA: 20s - loss: 0.4070 - hinge_accuracy: 0.8401"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "215/324 [==================>...........] - ETA: 20s - loss: 0.4073 - hinge_accuracy: 0.8398"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "216/324 [===================>..........] - ETA: 20s - loss: 0.4082 - hinge_accuracy: 0.8393"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "217/324 [===================>..........] - ETA: 20s - loss: 0.4087 - hinge_accuracy: 0.8387"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "218/324 [===================>..........] - ETA: 19s - loss: 0.4083 - hinge_accuracy: 0.8389"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "219/324 [===================>..........] - ETA: 19s - loss: 0.4084 - hinge_accuracy: 0.8388"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "220/324 [===================>..........] - ETA: 19s - loss: 0.4078 - hinge_accuracy: 0.8391"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "221/324 [===================>..........] - ETA: 19s - loss: 0.4075 - hinge_accuracy: 0.8392"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "222/324 [===================>..........] - ETA: 19s - loss: 0.4073 - hinge_accuracy: 0.8394"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "223/324 [===================>..........] - ETA: 18s - loss: 0.4068 - hinge_accuracy: 0.8395"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "224/324 [===================>..........] - ETA: 18s - loss: 0.4069 - hinge_accuracy: 0.8397"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "225/324 [===================>..........] - ETA: 18s - loss: 0.4070 - hinge_accuracy: 0.8394"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "226/324 [===================>..........] - ETA: 18s - loss: 0.4067 - hinge_accuracy: 0.8396"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "227/324 [====================>.........] - ETA: 18s - loss: 0.4070 - hinge_accuracy: 0.8391"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "228/324 [====================>.........] - ETA: 18s - loss: 0.4068 - hinge_accuracy: 0.8391"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "229/324 [====================>.........] - ETA: 17s - loss: 0.4065 - hinge_accuracy: 0.8392"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "230/324 [====================>.........] - ETA: 17s - loss: 0.4057 - hinge_accuracy: 0.8398"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "231/324 [====================>.........] - ETA: 17s - loss: 0.4063 - hinge_accuracy: 0.8396"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "232/324 [====================>.........] - ETA: 17s - loss: 0.4059 - hinge_accuracy: 0.8400"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "233/324 [====================>.........] - ETA: 17s - loss: 0.4054 - hinge_accuracy: 0.8401"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "234/324 [====================>.........] - ETA: 16s - loss: 0.4053 - hinge_accuracy: 0.8401"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "235/324 [====================>.........] - ETA: 16s - loss: 0.4053 - hinge_accuracy: 0.8402"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "236/324 [====================>.........] - ETA: 16s - loss: 0.4055 - hinge_accuracy: 0.8400"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "237/324 [====================>.........] - ETA: 16s - loss: 0.4059 - hinge_accuracy: 0.8398"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "238/324 [=====================>........] - ETA: 16s - loss: 0.4052 - hinge_accuracy: 0.8401"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "239/324 [=====================>........] - ETA: 15s - loss: 0.4053 - hinge_accuracy: 0.8402"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "240/324 [=====================>........] - ETA: 15s - loss: 0.4047 - hinge_accuracy: 0.8406"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "241/324 [=====================>........] - ETA: 15s - loss: 0.4037 - hinge_accuracy: 0.8412"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "242/324 [=====================>........] - ETA: 15s - loss: 0.4035 - hinge_accuracy: 0.8413"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "243/324 [=====================>........] - ETA: 15s - loss: 0.4037 - hinge_accuracy: 0.8410"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "244/324 [=====================>........] - ETA: 15s - loss: 0.4037 - hinge_accuracy: 0.8411"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "245/324 [=====================>........] - ETA: 14s - loss: 0.4033 - hinge_accuracy: 0.8412"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "246/324 [=====================>........] - ETA: 14s - loss: 0.4033 - hinge_accuracy: 0.8411"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "247/324 [=====================>........] - ETA: 14s - loss: 0.4030 - hinge_accuracy: 0.8411"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "248/324 [=====================>........] - ETA: 14s - loss: 0.4030 - hinge_accuracy: 0.8412"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "249/324 [======================>.......] - ETA: 14s - loss: 0.4029 - hinge_accuracy: 0.8414"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "250/324 [======================>.......] - ETA: 13s - loss: 0.4029 - hinge_accuracy: 0.8414"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "251/324 [======================>.......] - ETA: 13s - loss: 0.4022 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "252/324 [======================>.......] - ETA: 13s - loss: 0.4016 - hinge_accuracy: 0.8420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "253/324 [======================>.......] - ETA: 13s - loss: 0.4014 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "254/324 [======================>.......] - ETA: 13s - loss: 0.4011 - hinge_accuracy: 0.8422"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "255/324 [======================>.......] - ETA: 12s - loss: 0.4008 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "256/324 [======================>.......] - ETA: 12s - loss: 0.4008 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "257/324 [======================>.......] - ETA: 12s - loss: 0.4014 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "258/324 [======================>.......] - ETA: 12s - loss: 0.4015 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "259/324 [======================>.......] - ETA: 12s - loss: 0.4016 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "260/324 [=======================>......] - ETA: 12s - loss: 0.4013 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "261/324 [=======================>......] - ETA: 11s - loss: 0.4010 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "262/324 [=======================>......] - ETA: 11s - loss: 0.4009 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "263/324 [=======================>......] - ETA: 11s - loss: 0.4010 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "264/324 [=======================>......] - ETA: 11s - loss: 0.4009 - hinge_accuracy: 0.8422"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "265/324 [=======================>......] - ETA: 11s - loss: 0.4002 - hinge_accuracy: 0.8425"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "266/324 [=======================>......] - ETA: 10s - loss: 0.4002 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "267/324 [=======================>......] - ETA: 10s - loss: 0.4002 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "268/324 [=======================>......] - ETA: 10s - loss: 0.3998 - hinge_accuracy: 0.8425"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "269/324 [=======================>......] - ETA: 10s - loss: 0.4005 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "270/324 [========================>.....] - ETA: 10s - loss: 0.4003 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "271/324 [========================>.....] - ETA: 9s - loss: 0.4002 - hinge_accuracy: 0.8418 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "272/324 [========================>.....] - ETA: 9s - loss: 0.4007 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "273/324 [========================>.....] - ETA: 9s - loss: 0.4003 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "274/324 [========================>.....] - ETA: 9s - loss: 0.4004 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "275/324 [========================>.....] - ETA: 9s - loss: 0.4002 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "276/324 [========================>.....] - ETA: 9s - loss: 0.4000 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "277/324 [========================>.....] - ETA: 8s - loss: 0.3997 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "278/324 [========================>.....] - ETA: 8s - loss: 0.3996 - hinge_accuracy: 0.8420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "279/324 [========================>.....] - ETA: 8s - loss: 0.3988 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "280/324 [========================>.....] - ETA: 8s - loss: 0.3986 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "281/324 [=========================>....] - ETA: 8s - loss: 0.3984 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "282/324 [=========================>....] - ETA: 7s - loss: 0.3985 - hinge_accuracy: 0.8420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "283/324 [=========================>....] - ETA: 7s - loss: 0.3983 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "284/324 [=========================>....] - ETA: 7s - loss: 0.3979 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "285/324 [=========================>....] - ETA: 7s - loss: 0.3976 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "286/324 [=========================>....] - ETA: 7s - loss: 0.3976 - hinge_accuracy: 0.8422"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "287/324 [=========================>....] - ETA: 6s - loss: 0.3970 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "288/324 [=========================>....] - ETA: 6s - loss: 0.3971 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "289/324 [=========================>....] - ETA: 6s - loss: 0.3978 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "290/324 [=========================>....] - ETA: 6s - loss: 0.3977 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "291/324 [=========================>....] - ETA: 6s - loss: 0.3976 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "292/324 [==========================>...] - ETA: 6s - loss: 0.3978 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "293/324 [==========================>...] - ETA: 5s - loss: 0.3979 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "294/324 [==========================>...] - ETA: 5s - loss: 0.3981 - hinge_accuracy: 0.8416"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "295/324 [==========================>...] - ETA: 5s - loss: 0.3986 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "296/324 [==========================>...] - ETA: 5s - loss: 0.3984 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "297/324 [==========================>...] - ETA: 5s - loss: 0.3979 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "298/324 [==========================>...] - ETA: 4s - loss: 0.3979 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "299/324 [==========================>...] - ETA: 4s - loss: 0.3976 - hinge_accuracy: 0.8420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "300/324 [==========================>...] - ETA: 4s - loss: 0.3973 - hinge_accuracy: 0.8421"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "301/324 [==========================>...] - ETA: 4s - loss: 0.3972 - hinge_accuracy: 0.8420"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "302/324 [==========================>...] - ETA: 4s - loss: 0.3975 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "303/324 [===========================>..] - ETA: 3s - loss: 0.3979 - hinge_accuracy: 0.8414"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "304/324 [===========================>..] - ETA: 3s - loss: 0.3977 - hinge_accuracy: 0.8414"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "305/324 [===========================>..] - ETA: 3s - loss: 0.3975 - hinge_accuracy: 0.8413"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "306/324 [===========================>..] - ETA: 3s - loss: 0.3972 - hinge_accuracy: 0.8415"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "307/324 [===========================>..] - ETA: 3s - loss: 0.3973 - hinge_accuracy: 0.8417"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "308/324 [===========================>..] - ETA: 3s - loss: 0.3969 - hinge_accuracy: 0.8419"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "309/324 [===========================>..] - ETA: 2s - loss: 0.3973 - hinge_accuracy: 0.8418"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "310/324 [===========================>..] - ETA: 2s - loss: 0.3967 - hinge_accuracy: 0.8423"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "311/324 [===========================>..] - ETA: 2s - loss: 0.3961 - hinge_accuracy: 0.8427"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "312/324 [===========================>..] - ETA: 2s - loss: 0.3961 - hinge_accuracy: 0.8427"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "313/324 [===========================>..] - ETA: 2s - loss: 0.3961 - hinge_accuracy: 0.8430"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "314/324 [============================>.] - ETA: 1s - loss: 0.3960 - hinge_accuracy: 0.8429"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "315/324 [============================>.] - ETA: 1s - loss: 0.3960 - hinge_accuracy: 0.8427"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "316/324 [============================>.] - ETA: 1s - loss: 0.3957 - hinge_accuracy: 0.8429"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "317/324 [============================>.] - ETA: 1s - loss: 0.3957 - hinge_accuracy: 0.8431"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "318/324 [============================>.] - ETA: 1s - loss: 0.3957 - hinge_accuracy: 0.8433"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "319/324 [============================>.] - ETA: 0s - loss: 0.3960 - hinge_accuracy: 0.8432"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "320/324 [============================>.] - ETA: 0s - loss: 0.3958 - hinge_accuracy: 0.8433"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "321/324 [============================>.] - ETA: 0s - loss: 0.3956 - hinge_accuracy: 0.8436"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "322/324 [============================>.] - ETA: 0s - loss: 0.3958 - hinge_accuracy: 0.8437"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "323/324 [============================>.] - ETA: 0s - loss: 0.3959 - hinge_accuracy: 0.8437"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - ETA: 0s - loss: 0.3958 - hinge_accuracy: 0.8441"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - 63s 196ms/step - loss: 0.3958 - hinge_accuracy: 0.8441 - val_loss: 0.3608 - val_hinge_accuracy: 0.9088\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 3/3\n",
      "\r",
      "  1/324 [..............................] - ETA: 58s - loss: 0.2778 - hinge_accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  2/324 [..............................] - ETA: 1:01 - loss: 0.3483 - hinge_accuracy: 0.8125"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  3/324 [..............................] - ETA: 1:00 - loss: 0.3218 - hinge_accuracy: 0.8646"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  4/324 [..............................] - ETA: 1:00 - loss: 0.3295 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  5/324 [..............................] - ETA: 59s - loss: 0.3617 - hinge_accuracy: 0.8813 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  6/324 [..............................] - ETA: 59s - loss: 0.3464 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  7/324 [..............................] - ETA: 59s - loss: 0.3525 - hinge_accuracy: 0.8795"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  8/324 [..............................] - ETA: 59s - loss: 0.3555 - hinge_accuracy: 0.8828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "  9/324 [..............................] - ETA: 59s - loss: 0.3467 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 10/324 [..............................] - ETA: 59s - loss: 0.3481 - hinge_accuracy: 0.8844"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 11/324 [>.............................] - ETA: 58s - loss: 0.3487 - hinge_accuracy: 0.8864"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 12/324 [>.............................] - ETA: 58s - loss: 0.3594 - hinge_accuracy: 0.8828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 13/324 [>.............................] - ETA: 58s - loss: 0.3603 - hinge_accuracy: 0.8870"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 14/324 [>.............................] - ETA: 58s - loss: 0.3641 - hinge_accuracy: 0.8862"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 15/324 [>.............................] - ETA: 58s - loss: 0.3646 - hinge_accuracy: 0.8833"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 16/324 [>.............................] - ETA: 57s - loss: 0.3659 - hinge_accuracy: 0.8828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 17/324 [>.............................] - ETA: 57s - loss: 0.3571 - hinge_accuracy: 0.8842"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 18/324 [>.............................] - ETA: 57s - loss: 0.3595 - hinge_accuracy: 0.8802"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 19/324 [>.............................] - ETA: 57s - loss: 0.3544 - hinge_accuracy: 0.8832"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 20/324 [>.............................] - ETA: 57s - loss: 0.3546 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 21/324 [>.............................] - ETA: 56s - loss: 0.3573 - hinge_accuracy: 0.8869"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 22/324 [=>............................] - ETA: 56s - loss: 0.3497 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 23/324 [=>............................] - ETA: 56s - loss: 0.3499 - hinge_accuracy: 0.8927"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 24/324 [=>............................] - ETA: 56s - loss: 0.3471 - hinge_accuracy: 0.8932"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 25/324 [=>............................] - ETA: 56s - loss: 0.3466 - hinge_accuracy: 0.8950"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 26/324 [=>............................] - ETA: 55s - loss: 0.3441 - hinge_accuracy: 0.8990"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 27/324 [=>............................] - ETA: 55s - loss: 0.3463 - hinge_accuracy: 0.8981"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 28/324 [=>............................] - ETA: 55s - loss: 0.3429 - hinge_accuracy: 0.9007"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 29/324 [=>............................] - ETA: 55s - loss: 0.3470 - hinge_accuracy: 0.8987"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 30/324 [=>............................] - ETA: 55s - loss: 0.3479 - hinge_accuracy: 0.8979"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 31/324 [=>............................] - ETA: 54s - loss: 0.3482 - hinge_accuracy: 0.8962"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 32/324 [=>............................] - ETA: 54s - loss: 0.3487 - hinge_accuracy: 0.8955"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 33/324 [==>...........................] - ETA: 54s - loss: 0.3520 - hinge_accuracy: 0.8939"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 34/324 [==>...........................] - ETA: 54s - loss: 0.3497 - hinge_accuracy: 0.8952"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 35/324 [==>...........................] - ETA: 54s - loss: 0.3508 - hinge_accuracy: 0.8938"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 36/324 [==>...........................] - ETA: 54s - loss: 0.3501 - hinge_accuracy: 0.8941"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 37/324 [==>...........................] - ETA: 53s - loss: 0.3537 - hinge_accuracy: 0.8927"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 38/324 [==>...........................] - ETA: 53s - loss: 0.3560 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 39/324 [==>...........................] - ETA: 53s - loss: 0.3548 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 40/324 [==>...........................] - ETA: 53s - loss: 0.3596 - hinge_accuracy: 0.8883"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 41/324 [==>...........................] - ETA: 53s - loss: 0.3614 - hinge_accuracy: 0.8872"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 42/324 [==>...........................] - ETA: 52s - loss: 0.3612 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 43/324 [==>...........................] - ETA: 52s - loss: 0.3620 - hinge_accuracy: 0.8837"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 44/324 [===>..........................] - ETA: 52s - loss: 0.3638 - hinge_accuracy: 0.8842"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 45/324 [===>..........................] - ETA: 52s - loss: 0.3613 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 46/324 [===>..........................] - ETA: 52s - loss: 0.3621 - hinge_accuracy: 0.8852"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 47/324 [===>..........................] - ETA: 51s - loss: 0.3632 - hinge_accuracy: 0.8843"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 48/324 [===>..........................] - ETA: 51s - loss: 0.3644 - hinge_accuracy: 0.8835"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 49/324 [===>..........................] - ETA: 51s - loss: 0.3660 - hinge_accuracy: 0.8839"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 50/324 [===>..........................] - ETA: 51s - loss: 0.3663 - hinge_accuracy: 0.8831"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 51/324 [===>..........................] - ETA: 51s - loss: 0.3676 - hinge_accuracy: 0.8805"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 52/324 [===>..........................] - ETA: 50s - loss: 0.3659 - hinge_accuracy: 0.8804"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 53/324 [===>..........................] - ETA: 50s - loss: 0.3663 - hinge_accuracy: 0.8803"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 54/324 [====>.........................] - ETA: 50s - loss: 0.3669 - hinge_accuracy: 0.8808"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 55/324 [====>.........................] - ETA: 50s - loss: 0.3655 - hinge_accuracy: 0.8824"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 56/324 [====>.........................] - ETA: 50s - loss: 0.3637 - hinge_accuracy: 0.8828"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 57/324 [====>.........................] - ETA: 50s - loss: 0.3641 - hinge_accuracy: 0.8832"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 58/324 [====>.........................] - ETA: 49s - loss: 0.3619 - hinge_accuracy: 0.8847"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 59/324 [====>.........................] - ETA: 49s - loss: 0.3628 - hinge_accuracy: 0.8845"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 60/324 [====>.........................] - ETA: 49s - loss: 0.3628 - hinge_accuracy: 0.8844"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 61/324 [====>.........................] - ETA: 49s - loss: 0.3626 - hinge_accuracy: 0.8847"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 62/324 [====>.........................] - ETA: 49s - loss: 0.3632 - hinge_accuracy: 0.8851"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 63/324 [====>.........................] - ETA: 48s - loss: 0.3613 - hinge_accuracy: 0.8864"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 64/324 [====>.........................] - ETA: 48s - loss: 0.3601 - hinge_accuracy: 0.8872"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 65/324 [=====>........................] - ETA: 48s - loss: 0.3602 - hinge_accuracy: 0.8865"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 66/324 [=====>........................] - ETA: 48s - loss: 0.3606 - hinge_accuracy: 0.8864"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 67/324 [=====>........................] - ETA: 48s - loss: 0.3594 - hinge_accuracy: 0.8867"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 68/324 [=====>........................] - ETA: 48s - loss: 0.3583 - hinge_accuracy: 0.8879"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 69/324 [=====>........................] - ETA: 47s - loss: 0.3574 - hinge_accuracy: 0.8881"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 70/324 [=====>........................] - ETA: 47s - loss: 0.3584 - hinge_accuracy: 0.8884"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 71/324 [=====>........................] - ETA: 47s - loss: 0.3596 - hinge_accuracy: 0.8882"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 72/324 [=====>........................] - ETA: 47s - loss: 0.3578 - hinge_accuracy: 0.8893"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 73/324 [=====>........................] - ETA: 47s - loss: 0.3576 - hinge_accuracy: 0.8896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 74/324 [=====>........................] - ETA: 46s - loss: 0.3569 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 75/324 [=====>........................] - ETA: 46s - loss: 0.3572 - hinge_accuracy: 0.8896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 76/324 [======>.......................] - ETA: 46s - loss: 0.3573 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 77/324 [======>.......................] - ETA: 46s - loss: 0.3568 - hinge_accuracy: 0.8904"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 78/324 [======>.......................] - ETA: 46s - loss: 0.3569 - hinge_accuracy: 0.8902"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 79/324 [======>.......................] - ETA: 46s - loss: 0.3559 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 80/324 [======>.......................] - ETA: 45s - loss: 0.3557 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 81/324 [======>.......................] - ETA: 45s - loss: 0.3558 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 82/324 [======>.......................] - ETA: 45s - loss: 0.3579 - hinge_accuracy: 0.8895"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 83/324 [======>.......................] - ETA: 45s - loss: 0.3583 - hinge_accuracy: 0.8886"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 84/324 [======>.......................] - ETA: 45s - loss: 0.3573 - hinge_accuracy: 0.8891"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 85/324 [======>.......................] - ETA: 44s - loss: 0.3601 - hinge_accuracy: 0.8882"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 86/324 [======>.......................] - ETA: 44s - loss: 0.3607 - hinge_accuracy: 0.8881"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 87/324 [=======>......................] - ETA: 44s - loss: 0.3606 - hinge_accuracy: 0.8879"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 88/324 [=======>......................] - ETA: 44s - loss: 0.3616 - hinge_accuracy: 0.8878"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 89/324 [=======>......................] - ETA: 44s - loss: 0.3613 - hinge_accuracy: 0.8883"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 90/324 [=======>......................] - ETA: 43s - loss: 0.3612 - hinge_accuracy: 0.8885"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 91/324 [=======>......................] - ETA: 43s - loss: 0.3603 - hinge_accuracy: 0.8894"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 92/324 [=======>......................] - ETA: 43s - loss: 0.3595 - hinge_accuracy: 0.8896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 93/324 [=======>......................] - ETA: 43s - loss: 0.3601 - hinge_accuracy: 0.8884"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 94/324 [=======>......................] - ETA: 43s - loss: 0.3595 - hinge_accuracy: 0.8890"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 95/324 [=======>......................] - ETA: 43s - loss: 0.3590 - hinge_accuracy: 0.8888"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 96/324 [=======>......................] - ETA: 42s - loss: 0.3591 - hinge_accuracy: 0.8887"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 97/324 [=======>......................] - ETA: 42s - loss: 0.3599 - hinge_accuracy: 0.8882"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 98/324 [========>.....................] - ETA: 42s - loss: 0.3610 - hinge_accuracy: 0.8878"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 99/324 [========>.....................] - ETA: 42s - loss: 0.3608 - hinge_accuracy: 0.8879"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "100/324 [========>.....................] - ETA: 42s - loss: 0.3604 - hinge_accuracy: 0.8888"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "101/324 [========>.....................] - ETA: 41s - loss: 0.3608 - hinge_accuracy: 0.8883"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "102/324 [========>.....................] - ETA: 41s - loss: 0.3605 - hinge_accuracy: 0.8888"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "103/324 [========>.....................] - ETA: 41s - loss: 0.3615 - hinge_accuracy: 0.8880"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "104/324 [========>.....................] - ETA: 41s - loss: 0.3613 - hinge_accuracy: 0.8882"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "105/324 [========>.....................] - ETA: 41s - loss: 0.3622 - hinge_accuracy: 0.8875"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "106/324 [========>.....................] - ETA: 40s - loss: 0.3634 - hinge_accuracy: 0.8865"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "107/324 [========>.....................] - ETA: 40s - loss: 0.3620 - hinge_accuracy: 0.8873"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "108/324 [=========>....................] - ETA: 40s - loss: 0.3622 - hinge_accuracy: 0.8872"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "109/324 [=========>....................] - ETA: 40s - loss: 0.3627 - hinge_accuracy: 0.8873"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "110/324 [=========>....................] - ETA: 40s - loss: 0.3625 - hinge_accuracy: 0.8872"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "111/324 [=========>....................] - ETA: 39s - loss: 0.3627 - hinge_accuracy: 0.8868"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "112/324 [=========>....................] - ETA: 39s - loss: 0.3629 - hinge_accuracy: 0.8867"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "113/324 [=========>....................] - ETA: 39s - loss: 0.3632 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "114/324 [=========>....................] - ETA: 39s - loss: 0.3631 - hinge_accuracy: 0.8865"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "115/324 [=========>....................] - ETA: 39s - loss: 0.3630 - hinge_accuracy: 0.8867"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "116/324 [=========>....................] - ETA: 39s - loss: 0.3633 - hinge_accuracy: 0.8866"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "117/324 [=========>....................] - ETA: 38s - loss: 0.3637 - hinge_accuracy: 0.8862"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "118/324 [=========>....................] - ETA: 38s - loss: 0.3642 - hinge_accuracy: 0.8856"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "119/324 [==========>...................] - ETA: 38s - loss: 0.3637 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "120/324 [==========>...................] - ETA: 38s - loss: 0.3635 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "121/324 [==========>...................] - ETA: 38s - loss: 0.3635 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "122/324 [==========>...................] - ETA: 37s - loss: 0.3635 - hinge_accuracy: 0.8860"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "123/324 [==========>...................] - ETA: 37s - loss: 0.3632 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "124/324 [==========>...................] - ETA: 37s - loss: 0.3638 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "125/324 [==========>...................] - ETA: 37s - loss: 0.3633 - hinge_accuracy: 0.8860"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "126/324 [==========>...................] - ETA: 37s - loss: 0.3647 - hinge_accuracy: 0.8849"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "127/324 [==========>...................] - ETA: 36s - loss: 0.3644 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "128/324 [==========>...................] - ETA: 36s - loss: 0.3650 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "129/324 [==========>...................] - ETA: 36s - loss: 0.3656 - hinge_accuracy: 0.8852"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "130/324 [===========>..................] - ETA: 36s - loss: 0.3654 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "131/324 [===========>..................] - ETA: 36s - loss: 0.3653 - hinge_accuracy: 0.8850"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "132/324 [===========>..................] - ETA: 36s - loss: 0.3656 - hinge_accuracy: 0.8849"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "133/324 [===========>..................] - ETA: 35s - loss: 0.3658 - hinge_accuracy: 0.8851"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "134/324 [===========>..................] - ETA: 35s - loss: 0.3662 - hinge_accuracy: 0.8850"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "135/324 [===========>..................] - ETA: 35s - loss: 0.3661 - hinge_accuracy: 0.8850"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "136/324 [===========>..................] - ETA: 35s - loss: 0.3660 - hinge_accuracy: 0.8847"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "137/324 [===========>..................] - ETA: 35s - loss: 0.3650 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "138/324 [===========>..................] - ETA: 34s - loss: 0.3650 - hinge_accuracy: 0.8856"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "139/324 [===========>..................] - ETA: 34s - loss: 0.3655 - hinge_accuracy: 0.8856"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "140/324 [===========>..................] - ETA: 34s - loss: 0.3660 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "141/324 [============>.................] - ETA: 34s - loss: 0.3656 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "142/324 [============>.................] - ETA: 34s - loss: 0.3657 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "143/324 [============>.................] - ETA: 33s - loss: 0.3658 - hinge_accuracy: 0.8853"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "144/324 [============>.................] - ETA: 33s - loss: 0.3649 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "145/324 [============>.................] - ETA: 33s - loss: 0.3646 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "146/324 [============>.................] - ETA: 33s - loss: 0.3646 - hinge_accuracy: 0.8855"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "147/324 [============>.................] - ETA: 33s - loss: 0.3644 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "148/324 [============>.................] - ETA: 33s - loss: 0.3646 - hinge_accuracy: 0.8862"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "149/324 [============>.................] - ETA: 32s - loss: 0.3648 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "150/324 [============>.................] - ETA: 32s - loss: 0.3647 - hinge_accuracy: 0.8860"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "151/324 [============>.................] - ETA: 32s - loss: 0.3653 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "152/324 [=============>................] - ETA: 32s - loss: 0.3650 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "153/324 [=============>................] - ETA: 32s - loss: 0.3654 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "154/324 [=============>................] - ETA: 31s - loss: 0.3647 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "155/324 [=============>................] - ETA: 31s - loss: 0.3651 - hinge_accuracy: 0.8855"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "156/324 [=============>................] - ETA: 31s - loss: 0.3653 - hinge_accuracy: 0.8852"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "157/324 [=============>................] - ETA: 31s - loss: 0.3650 - hinge_accuracy: 0.8855"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "158/324 [=============>................] - ETA: 31s - loss: 0.3651 - hinge_accuracy: 0.8855"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "159/324 [=============>................] - ETA: 30s - loss: 0.3643 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "160/324 [=============>................] - ETA: 30s - loss: 0.3650 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "161/324 [=============>................] - ETA: 30s - loss: 0.3646 - hinge_accuracy: 0.8857"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "162/324 [==============>...............] - ETA: 30s - loss: 0.3647 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "163/324 [==============>...............] - ETA: 30s - loss: 0.3640 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "164/324 [==============>...............] - ETA: 30s - loss: 0.3647 - hinge_accuracy: 0.8859"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "165/324 [==============>...............] - ETA: 29s - loss: 0.3646 - hinge_accuracy: 0.8858"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "166/324 [==============>...............] - ETA: 29s - loss: 0.3648 - hinge_accuracy: 0.8857"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "167/324 [==============>...............] - ETA: 29s - loss: 0.3645 - hinge_accuracy: 0.8857"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "168/324 [==============>...............] - ETA: 29s - loss: 0.3641 - hinge_accuracy: 0.8856"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "169/324 [==============>...............] - ETA: 29s - loss: 0.3636 - hinge_accuracy: 0.8861"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "170/324 [==============>...............] - ETA: 28s - loss: 0.3634 - hinge_accuracy: 0.8864"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "171/324 [==============>...............] - ETA: 28s - loss: 0.3632 - hinge_accuracy: 0.8869"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "172/324 [==============>...............] - ETA: 28s - loss: 0.3630 - hinge_accuracy: 0.8870"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "173/324 [===============>..............] - ETA: 28s - loss: 0.3625 - hinge_accuracy: 0.8873"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "174/324 [===============>..............] - ETA: 28s - loss: 0.3619 - hinge_accuracy: 0.8878"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "175/324 [===============>..............] - ETA: 27s - loss: 0.3612 - hinge_accuracy: 0.8882"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "176/324 [===============>..............] - ETA: 27s - loss: 0.3610 - hinge_accuracy: 0.8885"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "177/324 [===============>..............] - ETA: 27s - loss: 0.3606 - hinge_accuracy: 0.8888"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "178/324 [===============>..............] - ETA: 27s - loss: 0.3599 - hinge_accuracy: 0.8890"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "179/324 [===============>..............] - ETA: 27s - loss: 0.3597 - hinge_accuracy: 0.8897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "180/324 [===============>..............] - ETA: 27s - loss: 0.3607 - hinge_accuracy: 0.8889"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "181/324 [===============>..............] - ETA: 26s - loss: 0.3603 - hinge_accuracy: 0.8892"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "182/324 [===============>..............] - ETA: 26s - loss: 0.3600 - hinge_accuracy: 0.8893"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "183/324 [===============>..............] - ETA: 26s - loss: 0.3604 - hinge_accuracy: 0.8890"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "184/324 [================>.............] - ETA: 26s - loss: 0.3603 - hinge_accuracy: 0.8891"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "185/324 [================>.............] - ETA: 26s - loss: 0.3600 - hinge_accuracy: 0.8894"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "186/324 [================>.............] - ETA: 25s - loss: 0.3598 - hinge_accuracy: 0.8894"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "187/324 [================>.............] - ETA: 25s - loss: 0.3593 - hinge_accuracy: 0.8897"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "188/324 [================>.............] - ETA: 25s - loss: 0.3585 - hinge_accuracy: 0.8900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "189/324 [================>.............] - ETA: 25s - loss: 0.3584 - hinge_accuracy: 0.8900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "190/324 [================>.............] - ETA: 25s - loss: 0.3587 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "191/324 [================>.............] - ETA: 24s - loss: 0.3588 - hinge_accuracy: 0.8894"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "192/324 [================>.............] - ETA: 24s - loss: 0.3590 - hinge_accuracy: 0.8893"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "193/324 [================>.............] - ETA: 24s - loss: 0.3583 - hinge_accuracy: 0.8896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "194/324 [================>.............] - ETA: 24s - loss: 0.3578 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "195/324 [=================>............] - ETA: 24s - loss: 0.3570 - hinge_accuracy: 0.8902"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "196/324 [=================>............] - ETA: 24s - loss: 0.3566 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "197/324 [=================>............] - ETA: 23s - loss: 0.3566 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "198/324 [=================>............] - ETA: 23s - loss: 0.3563 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "199/324 [=================>............] - ETA: 23s - loss: 0.3563 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "200/324 [=================>............] - ETA: 23s - loss: 0.3565 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "201/324 [=================>............] - ETA: 23s - loss: 0.3566 - hinge_accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "202/324 [=================>............] - ETA: 22s - loss: 0.3569 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "203/324 [=================>............] - ETA: 22s - loss: 0.3569 - hinge_accuracy: 0.8902"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "204/324 [=================>............] - ETA: 22s - loss: 0.3567 - hinge_accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "205/324 [=================>............] - ETA: 22s - loss: 0.3571 - hinge_accuracy: 0.8901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "206/324 [==================>...........] - ETA: 22s - loss: 0.3565 - hinge_accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "207/324 [==================>...........] - ETA: 21s - loss: 0.3564 - hinge_accuracy: 0.8904"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "208/324 [==================>...........] - ETA: 21s - loss: 0.3557 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "209/324 [==================>...........] - ETA: 21s - loss: 0.3555 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "210/324 [==================>...........] - ETA: 21s - loss: 0.3548 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "211/324 [==================>...........] - ETA: 21s - loss: 0.3543 - hinge_accuracy: 0.8917"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "212/324 [==================>...........] - ETA: 21s - loss: 0.3541 - hinge_accuracy: 0.8918"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "213/324 [==================>...........] - ETA: 20s - loss: 0.3542 - hinge_accuracy: 0.8916"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "214/324 [==================>...........] - ETA: 20s - loss: 0.3540 - hinge_accuracy: 0.8916"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "215/324 [==================>...........] - ETA: 20s - loss: 0.3541 - hinge_accuracy: 0.8916"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "216/324 [===================>..........] - ETA: 20s - loss: 0.3543 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "217/324 [===================>..........] - ETA: 20s - loss: 0.3542 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "218/324 [===================>..........] - ETA: 19s - loss: 0.3540 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "219/324 [===================>..........] - ETA: 19s - loss: 0.3535 - hinge_accuracy: 0.8918"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "220/324 [===================>..........] - ETA: 19s - loss: 0.3533 - hinge_accuracy: 0.8920"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "221/324 [===================>..........] - ETA: 19s - loss: 0.3539 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "222/324 [===================>..........] - ETA: 19s - loss: 0.3539 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "223/324 [===================>..........] - ETA: 18s - loss: 0.3546 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "224/324 [===================>..........] - ETA: 18s - loss: 0.3545 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "225/324 [===================>..........] - ETA: 18s - loss: 0.3548 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "226/324 [===================>..........] - ETA: 18s - loss: 0.3548 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "227/324 [====================>.........] - ETA: 18s - loss: 0.3545 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "228/324 [====================>.........] - ETA: 18s - loss: 0.3551 - hinge_accuracy: 0.8912"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "229/324 [====================>.........] - ETA: 17s - loss: 0.3554 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "230/324 [====================>.........] - ETA: 17s - loss: 0.3547 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "231/324 [====================>.........] - ETA: 17s - loss: 0.3546 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "232/324 [====================>.........] - ETA: 17s - loss: 0.3548 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "233/324 [====================>.........] - ETA: 17s - loss: 0.3547 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "234/324 [====================>.........] - ETA: 16s - loss: 0.3550 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "235/324 [====================>.........] - ETA: 16s - loss: 0.3556 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "236/324 [====================>.........] - ETA: 16s - loss: 0.3555 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "237/324 [====================>.........] - ETA: 16s - loss: 0.3555 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "238/324 [=====================>........] - ETA: 16s - loss: 0.3550 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "239/324 [=====================>........] - ETA: 15s - loss: 0.3555 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "240/324 [=====================>........] - ETA: 15s - loss: 0.3550 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "241/324 [=====================>........] - ETA: 15s - loss: 0.3553 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "242/324 [=====================>........] - ETA: 15s - loss: 0.3546 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "243/324 [=====================>........] - ETA: 15s - loss: 0.3545 - hinge_accuracy: 0.8912"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "244/324 [=====================>........] - ETA: 15s - loss: 0.3547 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "245/324 [=====================>........] - ETA: 14s - loss: 0.3543 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "246/324 [=====================>........] - ETA: 14s - loss: 0.3545 - hinge_accuracy: 0.8915"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "247/324 [=====================>........] - ETA: 14s - loss: 0.3545 - hinge_accuracy: 0.8916"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "248/324 [=====================>........] - ETA: 14s - loss: 0.3548 - hinge_accuracy: 0.8914"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "249/324 [======================>.......] - ETA: 14s - loss: 0.3550 - hinge_accuracy: 0.8912"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "250/324 [======================>.......] - ETA: 13s - loss: 0.3547 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "251/324 [======================>.......] - ETA: 13s - loss: 0.3546 - hinge_accuracy: 0.8911"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "252/324 [======================>.......] - ETA: 13s - loss: 0.3548 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "253/324 [======================>.......] - ETA: 13s - loss: 0.3546 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "254/324 [======================>.......] - ETA: 13s - loss: 0.3545 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "255/324 [======================>.......] - ETA: 12s - loss: 0.3544 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "256/324 [======================>.......] - ETA: 12s - loss: 0.3543 - hinge_accuracy: 0.8904"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "257/324 [======================>.......] - ETA: 12s - loss: 0.3542 - hinge_accuracy: 0.8904"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "258/324 [======================>.......] - ETA: 12s - loss: 0.3541 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "259/324 [======================>.......] - ETA: 12s - loss: 0.3539 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "260/324 [=======================>......] - ETA: 12s - loss: 0.3538 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "261/324 [=======================>......] - ETA: 11s - loss: 0.3534 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "262/324 [=======================>......] - ETA: 11s - loss: 0.3539 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "263/324 [=======================>......] - ETA: 11s - loss: 0.3540 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "264/324 [=======================>......] - ETA: 11s - loss: 0.3544 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "265/324 [=======================>......] - ETA: 11s - loss: 0.3545 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "266/324 [=======================>......] - ETA: 10s - loss: 0.3544 - hinge_accuracy: 0.8911"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "267/324 [=======================>......] - ETA: 10s - loss: 0.3542 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "268/324 [=======================>......] - ETA: 10s - loss: 0.3544 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "269/324 [=======================>......] - ETA: 10s - loss: 0.3545 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "270/324 [========================>.....] - ETA: 10s - loss: 0.3549 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "271/324 [========================>.....] - ETA: 9s - loss: 0.3554 - hinge_accuracy: 0.8903 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "272/324 [========================>.....] - ETA: 9s - loss: 0.3553 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "273/324 [========================>.....] - ETA: 9s - loss: 0.3553 - hinge_accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "274/324 [========================>.....] - ETA: 9s - loss: 0.3549 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "275/324 [========================>.....] - ETA: 9s - loss: 0.3546 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "276/324 [========================>.....] - ETA: 9s - loss: 0.3550 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "277/324 [========================>.....] - ETA: 8s - loss: 0.3554 - hinge_accuracy: 0.8900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "278/324 [========================>.....] - ETA: 8s - loss: 0.3557 - hinge_accuracy: 0.8896"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "279/324 [========================>.....] - ETA: 8s - loss: 0.3556 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "280/324 [========================>.....] - ETA: 8s - loss: 0.3554 - hinge_accuracy: 0.8900"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "281/324 [=========================>....] - ETA: 8s - loss: 0.3551 - hinge_accuracy: 0.8901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "282/324 [=========================>....] - ETA: 7s - loss: 0.3549 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "283/324 [=========================>....] - ETA: 7s - loss: 0.3552 - hinge_accuracy: 0.8901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "284/324 [=========================>....] - ETA: 7s - loss: 0.3549 - hinge_accuracy: 0.8902"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "285/324 [=========================>....] - ETA: 7s - loss: 0.3553 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "286/324 [=========================>....] - ETA: 7s - loss: 0.3552 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "287/324 [=========================>....] - ETA: 6s - loss: 0.3551 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "288/324 [=========================>....] - ETA: 6s - loss: 0.3554 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "289/324 [=========================>....] - ETA: 6s - loss: 0.3551 - hinge_accuracy: 0.8898"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "290/324 [=========================>....] - ETA: 6s - loss: 0.3549 - hinge_accuracy: 0.8899"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "291/324 [=========================>....] - ETA: 6s - loss: 0.3544 - hinge_accuracy: 0.8901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "292/324 [==========================>...] - ETA: 6s - loss: 0.3543 - hinge_accuracy: 0.8903"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "293/324 [==========================>...] - ETA: 5s - loss: 0.3539 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "294/324 [==========================>...] - ETA: 5s - loss: 0.3537 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "295/324 [==========================>...] - ETA: 5s - loss: 0.3539 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "296/324 [==========================>...] - ETA: 5s - loss: 0.3536 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "297/324 [==========================>...] - ETA: 5s - loss: 0.3533 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "298/324 [==========================>...] - ETA: 4s - loss: 0.3530 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "299/324 [==========================>...] - ETA: 4s - loss: 0.3532 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "300/324 [==========================>...] - ETA: 4s - loss: 0.3533 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "301/324 [==========================>...] - ETA: 4s - loss: 0.3532 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "302/324 [==========================>...] - ETA: 4s - loss: 0.3530 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "303/324 [===========================>..] - ETA: 3s - loss: 0.3531 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "304/324 [===========================>..] - ETA: 3s - loss: 0.3532 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "305/324 [===========================>..] - ETA: 3s - loss: 0.3533 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "306/324 [===========================>..] - ETA: 3s - loss: 0.3530 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "307/324 [===========================>..] - ETA: 3s - loss: 0.3534 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "308/324 [===========================>..] - ETA: 3s - loss: 0.3535 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "309/324 [===========================>..] - ETA: 2s - loss: 0.3539 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "310/324 [===========================>..] - ETA: 2s - loss: 0.3540 - hinge_accuracy: 0.8905"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "311/324 [===========================>..] - ETA: 2s - loss: 0.3539 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "312/324 [===========================>..] - ETA: 2s - loss: 0.3541 - hinge_accuracy: 0.8906"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "313/324 [===========================>..] - ETA: 2s - loss: 0.3539 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "314/324 [============================>.] - ETA: 1s - loss: 0.3539 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "315/324 [============================>.] - ETA: 1s - loss: 0.3536 - hinge_accuracy: 0.8909"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "316/324 [============================>.] - ETA: 1s - loss: 0.3532 - hinge_accuracy: 0.8911"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "317/324 [============================>.] - ETA: 1s - loss: 0.3536 - hinge_accuracy: 0.8911"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "318/324 [============================>.] - ETA: 1s - loss: 0.3538 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "319/324 [============================>.] - ETA: 0s - loss: 0.3541 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "320/324 [============================>.] - ETA: 0s - loss: 0.3540 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "321/324 [============================>.] - ETA: 0s - loss: 0.3536 - hinge_accuracy: 0.8907"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "322/324 [============================>.] - ETA: 0s - loss: 0.3533 - hinge_accuracy: 0.8908"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "323/324 [============================>.] - ETA: 0s - loss: 0.3533 - hinge_accuracy: 0.8910"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - ETA: 0s - loss: 0.3533 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "324/324 [==============================] - 63s 195ms/step - loss: 0.3533 - hinge_accuracy: 0.8913 - val_loss: 0.3449 - val_hinge_accuracy: 0.9062\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/62 [..............................] - ETA: 11s - loss: 0.4553 - hinge_accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/62 [>.............................] - ETA: 2s - loss: 0.4675 - hinge_accuracy: 0.8542 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/62 [=>............................] - ETA: 2s - loss: 0.4344 - hinge_accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/62 [==>...........................] - ETA: 2s - loss: 0.4294 - hinge_accuracy: 0.8795"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/62 [===>..........................] - ETA: 2s - loss: 0.4215 - hinge_accuracy: 0.8785"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/62 [====>.........................] - ETA: 2s - loss: 0.4322 - hinge_accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/62 [=====>........................] - ETA: 2s - loss: 0.4284 - hinge_accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/62 [======>.......................] - ETA: 2s - loss: 0.4226 - hinge_accuracy: 0.8833"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/62 [=======>......................] - ETA: 1s - loss: 0.4247 - hinge_accuracy: 0.8842"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/62 [========>.....................] - ETA: 1s - loss: 0.4236 - hinge_accuracy: 0.8832"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/62 [=========>....................] - ETA: 1s - loss: 0.4187 - hinge_accuracy: 0.8854"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/62 [==========>...................] - ETA: 1s - loss: 0.4076 - hinge_accuracy: 0.8913"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/62 [===========>..................] - ETA: 1s - loss: 0.4189 - hinge_accuracy: 0.8800"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/62 [============>.................] - ETA: 1s - loss: 0.4066 - hinge_accuracy: 0.8877"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/62 [=============>................] - ETA: 1s - loss: 0.4010 - hinge_accuracy: 0.8901"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "31/62 [==============>...............] - ETA: 1s - loss: 0.4012 - hinge_accuracy: 0.8881"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "33/62 [==============>...............] - ETA: 1s - loss: 0.3919 - hinge_accuracy: 0.8911"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "35/62 [===============>..............] - ETA: 1s - loss: 0.3855 - hinge_accuracy: 0.8964"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "37/62 [================>.............] - ETA: 1s - loss: 0.3822 - hinge_accuracy: 0.8986"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "39/62 [=================>............] - ETA: 0s - loss: 0.3778 - hinge_accuracy: 0.9006"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "41/62 [==================>...........] - ETA: 0s - loss: 0.3754 - hinge_accuracy: 0.8994"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "43/62 [===================>..........] - ETA: 0s - loss: 0.3731 - hinge_accuracy: 0.9004"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "45/62 [====================>.........] - ETA: 0s - loss: 0.3670 - hinge_accuracy: 0.9035"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "47/62 [=====================>........] - ETA: 0s - loss: 0.3616 - hinge_accuracy: 0.9049"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "49/62 [======================>.......] - ETA: 0s - loss: 0.3559 - hinge_accuracy: 0.9056"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "51/62 [=======================>......] - ETA: 0s - loss: 0.3535 - hinge_accuracy: 0.9075"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "53/62 [========================>.....] - ETA: 0s - loss: 0.3488 - hinge_accuracy: 0.9092"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "55/62 [=========================>....] - ETA: 0s - loss: 0.3452 - hinge_accuracy: 0.9097"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "57/62 [==========================>...] - ETA: 0s - loss: 0.3475 - hinge_accuracy: 0.9062"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "59/62 [===========================>..] - ETA: 0s - loss: 0.3426 - hinge_accuracy: 0.9078"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "61/62 [============================>.] - ETA: 0s - loss: 0.3441 - hinge_accuracy: 0.9078"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "62/62 [==============================] - 3s 43ms/step - loss: 0.3449 - hinge_accuracy: 0.9062\n"
     ]
    }
   ],
   "source": [
    "qnn_history = model.fit(\n",
    "      x_train_tfcirc_sub, y_train_hinge_sub,\n",
    "      batch_size=32,\n",
    "      epochs=EPOCHS,\n",
    "      verbose=1,\n",
    "      validation_data=(x_test_tfcirc, y_test_hinge))\n",
    "\n",
    "qnn_results = model.evaluate(x_test_tfcirc, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "3ER7B7aaojiP"
   },
   "source": [
    "Note: The training accuracy reports the average over the epoch. The validation accuracy is evaluated at the end of each epoch."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "8952YvuWGL7J"
   },
   "source": [
    "## 3. Classical neural network\n",
    "\n",
    "While the quantum neural network works for this simplified MNIST problem, a basic classical neural network can easily outperform a QNN on this task. After a single epoch, a classical neural network can achieve >98% accuracy on the holdout set.\n",
    "\n",
    "In the following example, a classical neural network is used for for the 3-6 classification problem using the entire 28x28 image instead of subsampling the image. This easily converges to nearly 100% accuracy of the test set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:41:43.660265Z",
     "iopub.status.busy": "2023-08-28T11:41:43.659603Z",
     "iopub.status.idle": "2023-08-28T11:41:43.719996Z",
     "shell.execute_reply": "2023-08-28T11:41:43.719312Z"
    },
    "id": "pZofEHhLGL7L"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_1\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " conv2d (Conv2D)             (None, 26, 26, 32)        320       \n",
      "                                                                 \n",
      " conv2d_1 (Conv2D)           (None, 24, 24, 64)        18496     \n",
      "                                                                 \n",
      " max_pooling2d (MaxPooling2D  (None, 12, 12, 64)       0         \n",
      " )                                                               \n",
      "                                                                 \n",
      " dropout (Dropout)           (None, 12, 12, 64)        0         \n",
      "                                                                 \n",
      " flatten (Flatten)           (None, 9216)              0         \n",
      "                                                                 \n",
      " dense (Dense)               (None, 128)               1179776   \n",
      "                                                                 \n",
      " dropout_1 (Dropout)         (None, 128)               0         \n",
      "                                                                 \n",
      " dense_1 (Dense)             (None, 1)                 129       \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 1,198,721\n",
      "Trainable params: 1,198,721\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "def create_classical_model():\n",
    "    # A simple model based off LeNet from https://keras.io/examples/mnist_cnn/\n",
    "    model = tf.keras.Sequential()\n",
    "    model.add(tf.keras.layers.Conv2D(32, [3, 3], activation='relu', input_shape=(28,28,1)))\n",
    "    model.add(tf.keras.layers.Conv2D(64, [3, 3], activation='relu'))\n",
    "    model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))\n",
    "    model.add(tf.keras.layers.Dropout(0.25))\n",
    "    model.add(tf.keras.layers.Flatten())\n",
    "    model.add(tf.keras.layers.Dense(128, activation='relu'))\n",
    "    model.add(tf.keras.layers.Dropout(0.5))\n",
    "    model.add(tf.keras.layers.Dense(1))\n",
    "    return model\n",
    "\n",
    "\n",
    "model = create_classical_model()\n",
    "model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),\n",
    "              optimizer=tf.keras.optimizers.Adam(),\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:41:43.723378Z",
     "iopub.status.busy": "2023-08-28T11:41:43.722772Z",
     "iopub.status.idle": "2023-08-28T11:41:47.405121Z",
     "shell.execute_reply": "2023-08-28T11:41:47.404371Z"
    },
    "id": "CiAJl7sZojiU"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/95 [..............................] - ETA: 51s - loss: 0.7019 - accuracy: 0.5000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 3/95 [..............................] - ETA: 2s - loss: 0.5220 - accuracy: 0.6771 "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 5/95 [>.............................] - ETA: 2s - loss: 0.3743 - accuracy: 0.8016"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 7/95 [=>............................] - ETA: 2s - loss: 0.2921 - accuracy: 0.8471"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      " 9/95 [=>............................] - ETA: 2s - loss: 0.2351 - accuracy: 0.8793"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "11/95 [==>...........................] - ETA: 2s - loss: 0.1976 - accuracy: 0.8999"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "13/95 [===>..........................] - ETA: 2s - loss: 0.1700 - accuracy: 0.9147"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "15/95 [===>..........................] - ETA: 2s - loss: 0.1537 - accuracy: 0.9250"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "17/95 [====>.........................] - ETA: 2s - loss: 0.1397 - accuracy: 0.9329"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "19/95 [=====>........................] - ETA: 2s - loss: 0.1301 - accuracy: 0.9383"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "21/95 [=====>........................] - ETA: 2s - loss: 0.1192 - accuracy: 0.9431"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "23/95 [======>.......................] - ETA: 1s - loss: 0.1188 - accuracy: 0.9463"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "25/95 [======>.......................] - ETA: 1s - loss: 0.1136 - accuracy: 0.9500"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "27/95 [=======>......................] - ETA: 1s - loss: 0.1059 - accuracy: 0.9537"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "29/95 [========>.....................] - ETA: 1s - loss: 0.0990 - accuracy: 0.9566"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "31/95 [========>.....................] - ETA: 1s - loss: 0.0931 - accuracy: 0.9592"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "33/95 [=========>....................] - ETA: 1s - loss: 0.0931 - accuracy: 0.9605"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "35/95 [==========>...................] - ETA: 1s - loss: 0.0906 - accuracy: 0.9621"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "37/95 [==========>...................] - ETA: 1s - loss: 0.0866 - accuracy: 0.9637"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "39/95 [===========>..................] - ETA: 1s - loss: 0.0846 - accuracy: 0.9649"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "41/95 [===========>..................] - ETA: 1s - loss: 0.0809 - accuracy: 0.9667"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "43/95 [============>.................] - ETA: 1s - loss: 0.0782 - accuracy: 0.9675"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "45/95 [=============>................] - ETA: 1s - loss: 0.0759 - accuracy: 0.9686"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "47/95 [=============>................] - ETA: 1s - loss: 0.0729 - accuracy: 0.9699"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "49/95 [==============>...............] - ETA: 1s - loss: 0.0704 - accuracy: 0.9711"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "51/95 [===============>..............] - ETA: 1s - loss: 0.0677 - accuracy: 0.9723"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "53/95 [===============>..............] - ETA: 1s - loss: 0.0657 - accuracy: 0.9730"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "55/95 [================>.............] - ETA: 1s - loss: 0.0636 - accuracy: 0.9739"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "57/95 [=================>............] - ETA: 1s - loss: 0.0620 - accuracy: 0.9744"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "59/95 [=================>............] - ETA: 0s - loss: 0.0602 - accuracy: 0.9752"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "61/95 [==================>...........] - ETA: 0s - loss: 0.0584 - accuracy: 0.9761"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "63/95 [==================>...........] - ETA: 0s - loss: 0.0571 - accuracy: 0.9766"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "65/95 [===================>..........] - ETA: 0s - loss: 0.0557 - accuracy: 0.9772"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "67/95 [====================>.........] - ETA: 0s - loss: 0.0545 - accuracy: 0.9777"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "69/95 [====================>.........] - ETA: 0s - loss: 0.0531 - accuracy: 0.9783"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "71/95 [=====================>........] - ETA: 0s - loss: 0.0517 - accuracy: 0.9789"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "73/95 [======================>.......] - ETA: 0s - loss: 0.0504 - accuracy: 0.9795"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "75/95 [======================>.......] - ETA: 0s - loss: 0.0492 - accuracy: 0.9799"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "77/95 [=======================>......] - ETA: 0s - loss: 0.0482 - accuracy: 0.9802"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "79/95 [=======================>......] - ETA: 0s - loss: 0.0471 - accuracy: 0.9807"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "81/95 [========================>.....] - ETA: 0s - loss: 0.0460 - accuracy: 0.9812"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "83/95 [=========================>....] - ETA: 0s - loss: 0.0450 - accuracy: 0.9816"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "85/95 [=========================>....] - ETA: 0s - loss: 0.0448 - accuracy: 0.9818"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "87/95 [==========================>...] - ETA: 0s - loss: 0.0440 - accuracy: 0.9821"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "89/95 [===========================>..] - ETA: 0s - loss: 0.0431 - accuracy: 0.9825"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "91/95 [===========================>..] - ETA: 0s - loss: 0.0422 - accuracy: 0.9829"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "93/95 [============================>.] - ETA: 0s - loss: 0.0414 - accuracy: 0.9833"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "95/95 [==============================] - 3s 30ms/step - loss: 0.0409 - accuracy: 0.9835 - val_loss: 0.0033 - val_accuracy: 0.9995\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/62 [..............................] - ETA: 1s - loss: 2.9011e-04 - accuracy: 1.0000"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "20/62 [========>.....................] - ETA: 0s - loss: 0.0065 - accuracy: 0.9984    "
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "39/62 [=================>............] - ETA: 0s - loss: 0.0042 - accuracy: 0.9992"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "58/62 [===========================>..] - ETA: 0s - loss: 0.0029 - accuracy: 0.9995"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "62/62 [==============================] - 0s 3ms/step - loss: 0.0033 - accuracy: 0.9995\n"
     ]
    }
   ],
   "source": [
    "model.fit(x_train,\n",
    "          y_train,\n",
    "          batch_size=128,\n",
    "          epochs=1,\n",
    "          verbose=1,\n",
    "          validation_data=(x_test, y_test))\n",
    "\n",
    "cnn_results = model.evaluate(x_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "X5-5BVJaojiZ"
   },
   "source": [
    "The above model has nearly 1.2M parameters. For a more fair comparison, try a 37-parameter model, on the subsampled images:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:41:47.409079Z",
     "iopub.status.busy": "2023-08-28T11:41:47.408437Z",
     "iopub.status.idle": "2023-08-28T11:41:47.437984Z",
     "shell.execute_reply": "2023-08-28T11:41:47.437315Z"
    },
    "id": "70TOM6r-ojiZ",
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Model: \"sequential_2\"\n",
      "_________________________________________________________________\n",
      " Layer (type)                Output Shape              Param #   \n",
      "=================================================================\n",
      " flatten_1 (Flatten)         (None, 16)                0         \n",
      "                                                                 \n",
      " dense_2 (Dense)             (None, 2)                 34        \n",
      "                                                                 \n",
      " dense_3 (Dense)             (None, 1)                 3         \n",
      "                                                                 \n",
      "=================================================================\n",
      "Total params: 37\n",
      "Trainable params: 37\n",
      "Non-trainable params: 0\n",
      "_________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "def create_fair_classical_model():\n",
    "    # A simple model based off LeNet from https://keras.io/examples/mnist_cnn/\n",
    "    model = tf.keras.Sequential()\n",
    "    model.add(tf.keras.layers.Flatten(input_shape=(4,4,1)))\n",
    "    model.add(tf.keras.layers.Dense(2, activation='relu'))\n",
    "    model.add(tf.keras.layers.Dense(1))\n",
    "    return model\n",
    "\n",
    "\n",
    "model = create_fair_classical_model()\n",
    "model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),\n",
    "              optimizer=tf.keras.optimizers.Adam(),\n",
    "              metrics=['accuracy'])\n",
    "\n",
    "model.summary()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:41:47.441164Z",
     "iopub.status.busy": "2023-08-28T11:41:47.440658Z",
     "iopub.status.idle": "2023-08-28T11:41:50.086442Z",
     "shell.execute_reply": "2023-08-28T11:41:50.085733Z"
    },
    "id": "lA_Fx-8gojid"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 1s - loss: 0.7137 - accuracy: 0.5251 - val_loss: 0.6860 - val_accuracy: 0.4873 - 547ms/epoch - 7ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 2/20\n",
      "81/81 - 0s - loss: 0.6755 - accuracy: 0.5251 - val_loss: 0.6504 - val_accuracy: 0.4878 - 100ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 3/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.6405 - accuracy: 0.5261 - val_loss: 0.6137 - val_accuracy: 0.4909 - 98ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 4/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.6014 - accuracy: 0.5370 - val_loss: 0.5699 - val_accuracy: 0.5127 - 100ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 5/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.5463 - accuracy: 0.5860 - val_loss: 0.4901 - val_accuracy: 0.6921 - 107ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 6/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.4607 - accuracy: 0.7678 - val_loss: 0.3997 - val_accuracy: 0.8171 - 103ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 7/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.3868 - accuracy: 0.8374 - val_loss: 0.3427 - val_accuracy: 0.8410 - 102ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 8/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.3377 - accuracy: 0.8585 - val_loss: 0.3057 - val_accuracy: 0.8562 - 102ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 9/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.3047 - accuracy: 0.8653 - val_loss: 0.2803 - val_accuracy: 0.8653 - 102ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 10/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2823 - accuracy: 0.8717 - val_loss: 0.2631 - val_accuracy: 0.8653 - 101ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 11/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2666 - accuracy: 0.8719 - val_loss: 0.2517 - val_accuracy: 0.8653 - 103ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 12/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2554 - accuracy: 0.8749 - val_loss: 0.2429 - val_accuracy: 0.9126 - 98ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 13/20\n",
      "81/81 - 0s - loss: 0.2473 - accuracy: 0.9000 - val_loss: 0.2369 - val_accuracy: 0.9126 - 100ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 14/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2412 - accuracy: 0.9005 - val_loss: 0.2324 - val_accuracy: 0.9136 - 102ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 15/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2367 - accuracy: 0.9009 - val_loss: 0.2290 - val_accuracy: 0.9136 - 101ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 16/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2333 - accuracy: 0.9009 - val_loss: 0.2266 - val_accuracy: 0.9136 - 101ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 17/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2306 - accuracy: 0.9010 - val_loss: 0.2245 - val_accuracy: 0.9136 - 99ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 18/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2284 - accuracy: 0.9010 - val_loss: 0.2231 - val_accuracy: 0.9136 - 100ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 19/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2266 - accuracy: 0.9013 - val_loss: 0.2217 - val_accuracy: 0.9146 - 102ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 20/20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "81/81 - 0s - loss: 0.2252 - accuracy: 0.9016 - val_loss: 0.2210 - val_accuracy: 0.9151 - 103ms/epoch - 1ms/step\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\r",
      " 1/62 [..............................] - ETA: 1s - loss: 0.4147 - accuracy: 0.8750"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "59/62 [===========================>..] - ETA: 0s - loss: 0.2195 - accuracy: 0.9158"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\r",
      "62/62 [==============================] - 0s 879us/step - loss: 0.2210 - accuracy: 0.9151\n"
     ]
    }
   ],
   "source": [
    "model.fit(x_train_bin,\n",
    "          y_train_nocon,\n",
    "          batch_size=128,\n",
    "          epochs=20,\n",
    "          verbose=2,\n",
    "          validation_data=(x_test_bin, y_test))\n",
    "\n",
    "fair_nn_results = model.evaluate(x_test_bin, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "colab_type": "text",
    "id": "RH3mam7EGL7N"
   },
   "source": [
    "## 4. Comparison\n",
    "\n",
    "Higher resolution input and a more powerful model make this problem easy for the CNN. While a classical model of similar power (~32 parameters) trains to a similar accuracy in a fraction of the time. One way or the other, the classical neural network easily outperforms the quantum neural network. For classical data, it is difficult to beat a classical neural network."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "colab": {},
    "colab_type": "code",
    "execution": {
     "iopub.execute_input": "2023-08-28T11:41:50.090273Z",
     "iopub.status.busy": "2023-08-28T11:41:50.089640Z",
     "iopub.status.idle": "2023-08-28T11:41:50.227091Z",
     "shell.execute_reply": "2023-08-28T11:41:50.226387Z"
    },
    "id": "NOMeN7pMGL7P"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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RYWCg4PdrtOtWzddddVV8vb2di7r06ePysvLVVtbKx8fnwbr+Pr6ytfX15OpAQCAFsqjMyM+Pj6KjIxUfn6+c1l9fb3y8/MVExPjdp3Bgwdr//79qq+vdy776quv1K1bN7chAgAAriwev03jcDi0dOlS/fnPf9bu3bv15JNPqrq62nl1TWJiolJSUpzjn3zySZ08eVKTJ0/WV199pbVr12r+/PmaNGnShXsWAACgxfL40t6EhAQdP35cqampKi8vV0REhPLy8pwfai0tLZWX1y+NExISog8++EBTp07VzTffrB49emjy5MmaPn36hXsWAACgxfI4RiQpOTlZycnJbh8rKChosCwmJkaffvppc3YFAABaOb6bBgAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgFDECAACMIkYAAIBRxAgAADCKGAEAAEYRIwAAwChiBAAAGEWMAAAAo4gRAABgVLNiJCsrS6GhofLz81N0dLS2bt3apPVWrFghm82mkSNHNme3AACgFfI4RlauXCmHw6G0tDTt2LFD/fv3V1xcnI4dO3bW9UpKSjRt2jTdcccdzZ4sAABofTyOkYyMDI0fP15JSUkKDw9Xdna2/P39lZOT0+g6dXV1evTRRzV37lz16tXrvCYMAABaF49ipLa2VkVFRYqNjf1lA15eio2NVWFhYaPr/fGPf1TXrl31+OOPN2k/NTU1qqqqcrkBAIDWyaMYqaysVF1dnex2u8tyu92u8vJyt+t88sknevvtt7V06dIm7yc9PV1BQUHOW0hIiCfTBAAALchFvZrm9OnTGj16tJYuXarOnTs3eb2UlBSdOnXKeSsrK7uIswQAACa18WRw586d5e3trYqKCpflFRUVCg4ObjD+wIEDKikpUXx8vHNZfX39Tztu00Z79+7Vb37zmwbr+fr6ytfX15OpAQCAFsqjMyM+Pj6KjIxUfn6+c1l9fb3y8/MVExPTYPyNN96oXbt2qbi42Hm7//77NXToUBUXF/P2CwAA8OzMiCQ5HA6NGTNGUVFRGjhwoDIzM1VdXa2kpCRJUmJionr06KH09HT5+fmpb9++Lut36NBBkhosBwAAVyaPYyQhIUHHjx9XamqqysvLFRERoby8POeHWktLS+XlxR92BQAATeNxjEhScnKykpOT3T5WUFBw1nVzc3Obs0sAANBKcQoDAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGAUMQIAAIxqVoxkZWUpNDRUfn5+io6O1tatWxsdu3TpUt1xxx3q2LGjOnbsqNjY2LOOBwAAVxaPY2TlypVyOBxKS0vTjh071L9/f8XFxenYsWNuxxcUFGjUqFHasGGDCgsLFRISorvvvltHjhw578kDAICWz+MYycjI0Pjx45WUlKTw8HBlZ2fL399fOTk5bse/8847mjhxoiIiInTjjTfqrbfeUn19vfLz88978gAAoOXzKEZqa2tVVFSk2NjYXzbg5aXY2FgVFhY2aRvff/+9fvjhB1199dWNjqmpqVFVVZXLDQAAtE4exUhlZaXq6upkt9tdltvtdpWXlzdpG9OnT1f37t1dgubX0tPTFRQU5LyFhIR4Mk0AANCCXNKraV566SWtWLFCq1evlp+fX6PjUlJSdOrUKeetrKzsEs4SAABcSm08Gdy5c2d5e3uroqLCZXlFRYWCg4PPuu6f/vQnvfTSS/roo4908803n3Wsr6+vfH19PZkaAABooTw6M+Lj46PIyEiXD5/+/GHUmJiYRtd75ZVXNG/ePOXl5SkqKqr5swUAAK2OR2dGJMnhcGjMmDGKiorSwIEDlZmZqerqaiUlJUmSEhMT1aNHD6Wnp0uSXn75ZaWmpmr58uUKDQ11frYkICBAAQEBF/CpAACAlsjjGElISNDx48eVmpqq8vJyRUREKC8vz/mh1tLSUnl5/XLCZfHixaqtrdXDDz/ssp20tDTNmTPn/GYPAABaPI9jRJKSk5OVnJzs9rGCggKX+yUlJc3ZBQAAuELw3TQAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOIEQAAYBQxAgAAjCJGAACAUcQIAAAwihgBAABGESMAAMAoYgQAABhFjAAAAKOaFSNZWVkKDQ2Vn5+foqOjtXXr1rOO//vf/64bb7xRfn5+6tevn9atW9esyQIAgNbH4xhZuXKlHA6H0tLStGPHDvXv319xcXE6duyY2/GbN2/WqFGj9Pjjj2vnzp0aOXKkRo4cqS+++OK8Jw8AAFo+j2MkIyND48ePV1JSksLDw5WdnS1/f3/l5OS4Hf/aa6/pnnvu0bPPPqs+ffpo3rx5uuWWW/Tmm2+e9+QBAEDL18aTwbW1tSoqKlJKSopzmZeXl2JjY1VYWOh2ncLCQjkcDpdlcXFxWrNmTaP7qampUU1NjfP+qVOnJElVVVWeTNdFXc2ZZq+L1ul8jqcL5fT/6kxPAZeRy+GY/PHMj6angMvI+R6TP69vWdZZx3kUI5WVlaqrq5PdbndZbrfbtWfPHrfrlJeXux1fXl7e6H7S09M1d+7cBstDQkI8mS5wVkFvTDA9BcBVepDpGQAugqZfmGPy9OnTCgpqfFsexcilkpKS4nI2pb6+XidPnlSnTp1ks9kMzqxlq6qqUkhIiMrKyhQYGGh6OoAkjktcfjgmLxzLsnT69Gl17979rOM8ipHOnTvL29tbFRUVLssrKioUHBzsdp3g4GCPxkuSr6+vfH19XZZ16NDBk6niLAIDA3mB4bLDcYnLDcfkhXG2MyI/8+gDrD4+PoqMjFR+fr5zWX19vfLz8xUTE+N2nZiYGJfxkrR+/fpGxwMAgCuLx2/TOBwOjRkzRlFRURo4cKAyMzNVXV2tpKQkSVJiYqJ69Oih9PR0SdLkyZM1ZMgQLViwQCNGjNCKFSu0fft2LVmy5MI+EwAA0CJ5HCMJCQk6fvy4UlNTVV5eroiICOXl5Tk/pFpaWiovr19OuAwaNEjLly/XrFmzNGPGDPXu3Vtr1qxR3759L9yzQJP4+voqLS2twVtggEkcl7jccExeejbrXNfbAAAAXER8Nw0AADCKGAEAAEYRIwAAwChiBLhC2Wy2s34tw4VSUFAgm82mb7/99oJsr6SkRDabTcXFxR6tt2TJEoWEhMjLy0uZmZlNWufOO+/UlClTnPdDQ0ObvC48xzF5bq31GCRGgFaovLxcTz31lHr16iVfX1+FhIQoPj6+wd/8uRQGDRqko0ePNukPH10sVVVVSk5O1vTp03XkyBE98cQTxuZypeKYdNXcY3Lbtm2t8vglRgwqKyvTY489pu7du8vHx0c9e/bU5MmTdeLEiUs+l1//BoiWq6SkRJGRkfr444/16quvateuXcrLy9PQoUM1adKkSz4fHx8fBQcHG/0qh9LSUv3www8aMWKEunXrJn9/f2NzuRJxTDbU3GOyS5cuZx37ww8/XKgpXlLEiCEHDx5UVFSU9u3bp7/97W/av3+/srOznX/N9uTJk6aniBZq4sSJstls2rp1q373u98pLCxMN910kxwOhz799NNG15s+fbrCwsLk7++vXr16afbs2S4/2D777DMNHTpU7du3V2BgoCIjI7V9+3ZJ0uHDhxUfH6+OHTuqXbt2uummm7Ru3TpJ7k+Jb9q0SXfeeaf8/f3VsWNHxcXF6ZtvvpEk5eXl6fbbb1eHDh3UqVMn3XfffTpw4ECz/z1yc3PVr18/SVKvXr1ks9lUUlKisWPHauTIkS5jp0yZojvvvLPZ+4J7HJOuGjsmDxw4oAceeEB2u10BAQG69dZb9dFHH7ms++u3aWw2mxYvXqz7779f7dq104svvtjseZlEjBgyadIk+fj46MMPP9SQIUN07bXXavjw4froo4905MgRzZw5U5L791A7dOig3Nxc5/1zvWDnzJmjiIgI/fWvf1VoaKiCgoL0hz/8QadPn5YkjR07Vv/+97/12muvyWazOV8Yubm5Db4TaM2aNS6/Tfy87ZycHF177bUKCAjQxIkTVVdXp1deeUXBwcHq2rVri32BtDQnT55UXl6eJk2apHbt2jV4/Gzf8dS+fXvl5ubqv//9r1577TUtXbpUCxcudD7+6KOP6pprrtG2bdtUVFSk559/XldddZWkn47nmpoabdy4Ubt27dLLL7+sgIAAt/spLi7WXXfdpfDwcBUWFuqTTz5RfHy86urqJEnV1dVyOBzavn278vPz5eXlpQcffFD19fXN+jdJSEhw/kDfunWrjh49yjeAX0Ickw01dkx+9913uvfee5Wfn6+dO3fqnnvuUXx8vEpLS8+6vTlz5ujBBx/Url279NhjjzVrTsZZuOROnDhh2Ww2a/78+W4fHz9+vNWxY0ervr7ekmStXr3a5fGgoCBr2bJlzvvz5s2zNm3aZB06dMh6//33Lbvdbr388svOx9PS0qyAgADroYcesnbt2mVt3LjRCg4OtmbMmGFZlmV9++23VkxMjDV+/Hjr6NGj1tGjR60ff/zRWrZsmRUUFOSy79WrV1v//7D5edsPP/yw9eWXX1rvv/++5ePjY8XFxVlPPfWUtWfPHisnJ8eSZH366afn9w+Hc9qyZYslyVq1atU5x7o7tv6/V1991YqMjHTeb9++vZWbm+t2bL9+/aw5c+a4fWzDhg2WJOubb76xLMuyRo0aZQ0ePPic8/vZ8ePHLUnWrl27LMuyrEOHDlmSrJ07dzZ5Gzt37rQkWYcOHXIuGzNmjPXAAw+4jJs8ebI1ZMgQ5/0hQ4ZYkydPdt7v2bOntXDhwibvFxyTjXF3TLpz0003WW+88Ybz/q+PQUnWlClTmrzfyxVnRgzYt2+fLMtSnz593D7ep08fffPNNzp+/HiTtjdr1iwNGjRIoaGhio+P17Rp0/Tuu++6jKmvr1dubq769u2rO+64Q6NHj3Z+cCwoKEg+Pj7y9/dXcHCwgoOD5e3t3eTnU19fr5ycHIWHhys+Pl5Dhw7V3r17lZmZqRtuuEFJSUm64YYbtGHDhiZvE81jnccfVF65cqUGDx6s4OBgBQQEaNasWS6/kTkcDo0bN06xsbF66aWXXE5TP/3003rhhRc0ePBgpaWl6fPPP290Pz//FtqYffv2adSoUerVq5cCAwMVGhoqSef87RCXJ47Jpvvuu+80bdo09enTRx06dFBAQIB27959zv1ERUVd0HmYQIwYdK4XqY+PT5O2c64XrPTT+4zt27d33u/WrZuOHTvm+aTd+PW27Xa7wsPDXb6jyG63X7D9oXG9e/eWzWbTnj17PFqvsLBQjz76qO69917961//0s6dOzVz5kzV1tY6x8yZM0dffvmlRowYoY8//ljh4eFavXq1JGncuHE6ePCgRo8erV27dikqKkpvvPGG2321bdv2rHOJj4/XyZMntXTpUm3ZskVbtmyRJJe5XAheXl4NXoMt9cN/lzOOyaabNm2aVq9erfnz5+s///mPiouL1a9fv3Pux93bXy0NMWLA9ddfL5vNpt27d7t9fPfu3erSpYs6dOggm8121h+YTXnBSnK+j/ozm812zvc7m/rD2t22m7M/nL+rr75acXFxysrKUnV1dYPHG/u7Cps3b1bPnj01c+ZMRUVFqXfv3jp8+HCDcWFhYZo6dao+/PBDPfTQQ1q2bJnzsZCQEE2YMEGrVq3SM888o6VLl7rd180339zo5ZwnTpzQ3r17NWvWLN11113Os4QXQ5cuXXT06FGXZZ7+nQicG8dk023atEljx47Vgw8+qH79+ik4OFglJSUXZV+XG2LEgE6dOmnYsGFatGiRzpw54/JYeXm53nnnHY0dO1ZSwx+Y+/bt0/fff++839QX7Ln4+Pg4P6z1sy5duuj06dMuP0D4YX35y8rKUl1dnQYOHKh//OMf2rdvn3bv3q3XX39dMTExbtfp3bu3SktLtWLFCh04cECvv/668zdMSTpz5oySk5NVUFCgw4cPa9OmTdq2bZvzrcYpU6bogw8+0KFDh7Rjxw5t2LCh0bchU1JStG3bNk2cOFGff/659uzZo8WLF6uyslIdO3ZUp06dtGTJEu3fv18ff/yxHA7Hhf9HkvTb3/5W27dv11/+8hft27dPaWlp+uKLLy7Kvq50HJNN07t3b61atUrFxcX67LPP9Mgjj1wxv8QRI4a8+eabqqmpUVxcnDZu3KiysjLl5eVp2LBhCgsLU2pqqqSffmC++eab2rlzp7Zv364JEya4nHU41wu2qUJDQ7VlyxaVlJSosrJS9fX1io6Olr+/v2bMmKEDBw5o+fLlLlfx4PLUq1cv7dixQ0OHDtUzzzyjvn37atiwYcrPz9fixYvdrnP//fdr6tSpSk5OVkREhDZv3qzZs2c7H/f29taJEyeUmJiosLAw/f73v9fw4cM1d+5cSVJdXZ0mTZqkPn366J577lFYWJgWLVrkdl9hYWH68MMP9dlnn2ngwIGKiYnRP//5T7Vp00ZeXl5asWKFioqK1LdvX02dOlWvvvrqOZ9zaGio5syZ49G/U1xcnGbPnq3nnntOt956q06fPq3ExESPtoGm4ZhsmoyMDHXs2FGDBg1SfHy84uLidMstt3i0jRbL4Idnr3iHDh2yxowZY9ntdstms1mSrIceesiqrq52jjly5Ih19913W+3atbN69+5trVu3rsHVNM8++6zVqVMnKyAgwEpISLAWLlzochVMWlqa1b9/f5d9L1y40OrZs6fz/t69e63bbrvNatu2rcsnvFevXm1df/31Vtu2ba377rvPWrJkSYOraX69bXdXKfz6qgTgQqmurrb8/PysDRs2mJ4KYFkWx2Rz2CzrPD7qjAsqLS1NGRkZWr9+vW677TbT0wFahLVr12rRokVau3at6akAkjgmm4MYucwsW7ZMp06d0tNPP+1yNQoAAK0VMQIAAIziV28AAGAUMQIAAIwiRgAAgFHECAAAMIoYAQAARhEjAADAKGIEAAAYRYwAAACjiBEAAGDU/wGaifkNJH8yfQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "qnn_accuracy = qnn_results[1]\n",
    "cnn_accuracy = cnn_results[1]\n",
    "fair_nn_accuracy = fair_nn_results[1]\n",
    "\n",
    "sns.barplot(x=[\"Quantum\", \"Classical, full\", \"Classical, fair\"],\n",
    "            y=[qnn_accuracy, cnn_accuracy, fair_nn_accuracy])"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "mnist.ipynb",
   "private_outputs": true,
   "provenance": [],
   "toc_visible": true
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  },
  "vscode": {
   "interpreter": {
    "hash": "916dbcbb3f70747c44a77c7bcd40155683ae19c65e1c03b4aa3499c5328201f1"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
