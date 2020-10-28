{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "khan=0\n",
    "correy=0\n",
    "li=0\n",
    "otooley=0\n",
    "mx=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "path = \"resources/election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(path, \"r\") as file:\n",
    "    csv_reader = csv.reader(file)\n",
    "    header = next(csv_reader)\n",
    "    data = [row for row in csv.reader(file)]\n",
    "    total=len(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in data:\n",
    "    if i[2] == \"Khan\":\n",
    "        khan+= 1\n",
    "    \n",
    "    elif i[2] == \"Correy\":\n",
    "        correy+=1\n",
    "    \n",
    "    elif i[2] == \"Li\":\n",
    "        li+=1\n",
    "    \n",
    "    elif i[2] == \"O'Tooley\":\n",
    "        otooley+=1\n",
    "\n",
    "    results=[khan,correy,li,otooley]\n",
    "    \n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "khan_percent = ((khan/total)*100)\n",
    "khan_rounded = \"{:.3f}\".format(khan_percent)\n",
    "\n",
    "correy_percent = ((correy/total)*100)\n",
    "correy_rounded = \"{:.3f}\".format(correy_percent)\n",
    "\n",
    "li_percent = ((li/total)*100)\n",
    "li_rounded = \"{:.3f}\".format(li_percent)\n",
    "\n",
    "otooley_percent = ((otooley/total)*100)\n",
    "otooley_rounded = \"{:.3f}\".format(otooley_percent)\n",
    "\n",
    "#print(type(khan_percent))\n",
    "#print(khan_limited)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "    if max(results) == khan:\n",
    "        winner=\"Khan\"\n",
    "\n",
    "    elif max(results) == correy:\n",
    "        winner=\"Correy\"\n",
    "\n",
    "    elif max(results) == li:\n",
    "        winner=\"Li\"\n",
    "\n",
    "    if max(results) == otooley:\n",
    "        winner=\"O'Tooley\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------\n",
      "Khan:  63.000 % 2218231\n",
      "Correy:  20.000 % 704200\n",
      "Li:  14.000 % 492940\n",
      "O'Tooley:  3.000 % 105630\n",
      "-------------------------\n",
      "Winner:  Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Election Results\")\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"Total Votes: \"+ str(total))\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"Khan: \",khan_rounded,\"%\",khan,)\n",
    "print(\"Correy: \",correy_rounded,\"%\",correy,)\n",
    "print(\"Li: \",li_rounded,\"%\",li,)\n",
    "print(\"O'Tooley: \",otooley_rounded,\"%\",otooley,)\n",
    "print(\"-------------------------\")\n",
    "\n",
    "print(\"Winner: \",winner,)\n",
    "print(\"-------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "2218231\n"
     ]
    }
   ],
   "source": [
    "khan_as_string = str(khan)\n",
    "correy_as_string =str(correy)\n",
    "li_as_string = str(li)\n",
    "otooley_as_string = str(otooley)\n",
    "\n",
    "#print(type(khan_as_string))\n",
    "#print(khan_as_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"PyPollOutput.txt\", 'w') as election_res:\n",
    "    election_res.writelines(\"Election Results\\n\")\n",
    "    election_res.writelines(\"-------------------------\\n\")\n",
    "    election_res.writelines(f\"Total Votes: {total}\\n\")\n",
    "    election_res.writelines(\"-------------------------\\n\")\n",
    "\n",
    "    election_res.writelines(f\"Khan: \")\n",
    "    election_res.writelines({khan_rounded})\n",
    "    election_res.writelines(f\"% (\")\n",
    "    election_res.writelines({khan_as_string})\n",
    "    election_res.writelines(f\")\\n\")\n",
    "    \n",
    "    election_res.writelines(f\"Correy: \")\n",
    "    election_res.writelines({correy_rounded})\n",
    "    election_res.writelines(f\"% (\")\n",
    "    election_res.writelines({correy_as_string})\n",
    "    election_res.writelines(f\")\\n\")\n",
    "\n",
    "    election_res.writelines(f\"Li: \")\n",
    "    election_res.writelines({li_rounded})\n",
    "    election_res.writelines(f\"% (\")\n",
    "    election_res.writelines({li_as_string})\n",
    "    election_res.writelines(f\")\\n\")\n",
    "\n",
    "    election_res.writelines(f\"O'Tooley: \")\n",
    "    election_res.writelines({otooley_rounded})\n",
    "    election_res.writelines(f\"% (\")\n",
    "    election_res.writelines({otooley_as_string})\n",
    "    election_res.writelines(f\")\\n\")\n",
    "    \n",
    "    election_res.writelines(\"-------------------------\\n\")\n",
    "    election_res.writelines(f\"Winner: \")\n",
    "    election_res.writelines({winner})\n",
    "    election_res.writelines(\"\\n-------------------------\\n\")"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
