# Finding available instruments[](#finding-available-instruments "Link to this heading")

Similar to the pyvisa’s ResourceManager, RsInstrument can search for available instruments:

```python
1""""
2Find the instruments in your environment.
3"""
4
5from RsInstrument import *
6
7# Use the instr_list string items as resource names in the RsInstrument constructor
8instr_list = RsInstrument.list_resources("?*")
9print(instr_list)
```

If you have more VISAs installed, the one actually used by default is defined by a secret widget called VISA Conflict Manager. You can force your program to use a VISA of your choice:

```python
 1"""
 2Find the instruments in your environment with the defined VISA implementation.
 3"""
 4
 5from RsInstrument import *
 6
 7# In the optional parameter visa_select you can use e.g.: 'rs' or 'ni'
 8# Rs Visa also finds any NRP-Zxx USB sensors
 9instr_list = RsInstrument.list_resources('?*', 'rs')
10print(instr_list)
```

Tip

We believe our R&S VISA is the best choice for our customers. Couple of reasons why:

* Small footprint
* Superior VXI-11 and HiSLIP performance
* Integrated legacy sensors NRP-Zxx support
* Additional VXI-11 and LXI devices search
* Available for Windows, Linux, Mac OS
