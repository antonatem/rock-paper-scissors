{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0. 0.]\n",
      " [0. 0. 0.]\n",
      " [0. 0. 0.]\n",
      " [0. 0. 0.]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# def guess():\n",
    "ACTION = ['R', 'P', 'S']\n",
    "Q = np.zeros((4, 3))\n",
    "\n",
    "# Define hyperparameters\n",
    "episodes = 1500\n",
    "learning_rate = 0.2\n",
    "gamma = 0.9\n",
    "\n",
    "# Define exploration parameters\n",
    "epsilon = 0.9\n",
    "\n",
    "if np.random.uniform(0, 1) < epsilon:\n",
    "    np.random.choice(ACTION, 1)\n",
    "else:\n",
    "    np.argmax(Q[state, :])\n",
    "\n",
    "# Q[state, action] = Q[state, action] + LEARNING_RATE * (reward + GAMMA * np.max(Q[new_state, :]) - Q[state, action])\n",
    "\n",
    "print(Q)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
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
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
