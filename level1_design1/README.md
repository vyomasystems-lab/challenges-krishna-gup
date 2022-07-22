# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

<img width="735" alt="image" src="https://user-images.githubusercontent.com/83169108/180520436-6741d501-6f8c-4fd8-961e-7fac0aeaeb7f.png">

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 

```
x = 1
dut.sel.value = x
dut.inp0.value = random.randint(0,3)
```

The design in the same way is checked on all possible combinantions of sel.

The assert statement is used for comparing the multiplexers's outut to the expected value.

The following error is seen:

<img width="616" alt="image" src="https://user-images.githubusercontent.com/83169108/180523568-fe4afd72-a02d-41c7-b2ce-f1bead3e2b01.png">

We can see that at binary 01100, the inputted value dosen't match with the outputted value for that select line, hence a bug is present here

Another bug could be seen here

<img width="611" alt="image" src="https://user-images.githubusercontent.com/83169108/180533144-e7c0ccf2-e2dd-4950-9b33-a2376b0f0b5e.png">

We can see that at binary 11110, there is another mismatch 

## Test Scenario
- Test Inputs: sel ranges from 0 to 30
- Expected Output: inp for respective sel should match with the output
- Observed Output in the DUT dut.out = 0, for input of 2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12; //BUGGY, inp 12 should be 5'b01100
      5'b01101: out = inp13;
      5'b01110: out = inp14;
```

```
     5'b11011: out = inp27;
      5'b11100: out = inp28;
      5'b11101: out = inp29; //BUGGY, inp 30 is missing
      default: out = 0;
    endcase
  end
```

## Design Fix
Updating the design and re-running the test makes the test pass.

<img width="610" alt="image" src="https://user-images.githubusercontent.com/83169108/180541921-17c17ac7-089a-41f7-a58f-276c38c66409.png">

The updated design is checked in as mux_fix.v

## Verification Strategy

Strategy is to check that when a particular selection line is turned on, that respective input line must get connected to the output, hence, we check it in a loop fasion for all possibilities of selection line and giving randomized inputs and matching them with outputs.

## Is the verification complete ?

Yes, the verification is completed
