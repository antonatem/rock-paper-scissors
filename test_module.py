{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "from RPS_game import play, mrugesh, abbey, quincy, kris\n",
    "from RPS import player\n",
    "\n",
    "\n",
    "class UnitTests(unittest.TestCase):\n",
    "    print()\n",
    "\n",
    "    def test_player_vs_quincy(self):\n",
    "        print(\"Testing game against quincy...\")\n",
    "        actual = play(player, quincy, 1000) >= 60\n",
    "        self.assertTrue(\n",
    "            actual,\n",
    "            'Expected player to defeat quincy at least 60% of the time.')\n",
    "\n",
    "    def test_player_vs_abbey(self):\n",
    "        print(\"Testing game against abbey...\")\n",
    "        actual = play(player, abbey, 1000) >= 60\n",
    "        self.assertTrue(\n",
    "            actual,\n",
    "            'Expected player to defeat abbey at least 60% of the time.')\n",
    "\n",
    "    def test_player_vs_kris(self):\n",
    "        print(\"Testing game against kris...\")\n",
    "        actual = play(player, kris, 1000) >= 60\n",
    "        self.assertTrue(\n",
    "            actual, 'Expected player to defeat kris at least 60% of the time.')\n",
    "\n",
    "    def test_player_vs_mrugesh(self):\n",
    "        print(\"Testing game against mrugesh...\")\n",
    "        actual = play(player, mrugesh, 1000) >= 60\n",
    "        self.assertTrue(\n",
    "            actual,\n",
    "            'Expected player to defeat mrugesh at least 60% of the time.')\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    unittest.main()\n"
   ]
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
