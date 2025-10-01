{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8bea85e2-46f4-465e-9e9f-aa9dd6c5b39c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# def greet(name): \n",
    "#     return f'Hello{neme}!'\n",
    "# pi_value=3.14\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ebbf2002-9583-455e-acb4-72fbe8bf380d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# import my_module \n",
    "# print(my_module.greet(suraj))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d420b6b1-7756-49bf-8c23-9ae935f86d83",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.14\n"
     ]
    }
   ],
   "source": [
    "import my_module\n",
    "print(pi_value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "625dc72e-e605-46e6-9dfd-53fc2befd982",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello suraj\n"
     ]
    }
   ],
   "source": [
    "import mymodule\n",
    "print(mymodule.greet(\"suraj\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "94522343-877b-42cf-a163-5a4ed75aa68b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pivalue' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[28]\u001b[39m\u001b[32m, line 2\u001b[39m\n\u001b[32m      1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mmymodule\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m2\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[43mpivalue\u001b[49m)\n",
      "\u001b[31mNameError\u001b[39m: name 'pivalue' is not defined"
     ]
    }
   ],
   "source": [
    "import mymodule\n",
    "print(pivalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "5416f685-3e46-4683-965b-b6cc82e9f238",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.14\n"
     ]
    }
   ],
   "source": [
    "import self_module\n",
    "print(pi_value)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
