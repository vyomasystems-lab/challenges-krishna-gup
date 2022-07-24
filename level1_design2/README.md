# Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

<img width="735" alt="image" src="https://user-images.githubusercontent.com/83169108/180520436-6741d501-6f8c-4fd8-961e-7fac0aeaeb7f.png">

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 

```
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut._log.info(f'OUT={dut.seq_seen.value} IN=1')
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    dut._log.info(f'OUT={dut.seq_seen.value} IN=10')
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut._log.info(f'OUT={dut.seq_seen.value} IN=101')
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    dut._log.info(f'OUT={dut.seq_seen.value} IN=1011')
```

The design at every clock edge holds the input, the input is fed in the desired sequence.

The assert statement is used for comparing the Design Under Test's output to the expected output.

The following error is seen:

<img width="568" alt="image" src="https://user-images.githubusercontent.com/83169108/180642973-abac9a01-49e3-4deb-aa62-882deeca4174.png">

We can see that when the whole sequence is inputted, the output isn't HIGH, it goes high at next clock cycle, hence a bug is present here

## Test Scenario
- Test Inputs: inp_bit: 1011 At every clock edge
- Expected Output: Upon inputting full sequence, output must go HIGH
- Observed Output in the DUT dut.seq_seen = 0, for input of 1011

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
  reg [2:0] current_state, next_state;

  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0; //BUGGY, It gets assigned in the next clock cycle

  // state transition
  always @(posedge clk)
```

## Design Fix
Updating the design and re-running the test makes the test pass.

<img width="374" alt="image" src="https://user-images.githubusercontent.com/83169108/180643918-d48b2ab0-67ab-4506-844a-4807219c67dc.png">

The updated design is checked in as seq_detect_1011_fix.v

## Verification Strategy

Strategy is to check that when the full input sequence is recieved, the output goes high immediately, not waiting till the next clock cycle, we test for random inputs and if the inputs are in correct sequence, we send HIGH as output.

## Is the verification complete ?

Yes, the verification is completed
