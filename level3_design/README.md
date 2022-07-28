# Elevator Controller Finite State Machine Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

<img width="735" alt="image" src="https://user-images.githubusercontent.com/83169108/180520436-6741d501-6f8c-4fd8-961e-7fac0aeaeb7f.png">

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test.
The values are assigned to the input port using 

```
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    req = 12

    dut.requested_floor.value = req
    await RisingEdge(dut.clk)
    
    for i in range(1,req+1):
        await RisingEdge(dut.clk)
        assert dut.y.value == i, "Wrong Outputs"
        dut._log.info(f'OUT={dut.y.value} UP={dut.Up.value}')

    await RisingEdge(dut.clk)
    assert (dut.Up.value == 0) | (dut.Down.value == 0), "Still Moving"
    assert dut.door.value == 1, "Door not open"
    assert dut.y.value == dut.requested_floor.value, "Wrong Floor"
```

The testbench inputs the desired floor and compares the outputs with the expected outputs from the design.

<img width="599" alt="image" src="https://user-images.githubusercontent.com/83169108/181639333-60924ac9-2df5-4acd-b6c7-c6f0656bd1f5.png">

We can see that the design is working perfectly and all cases for doors, motion etc. are correctly being checked and no errors are found.

## Inserting a BUG

In order to verify the functionality and the logic of my verification, we need to insert a bug into the design. The following bug is introduced into the code, and saved as fsm_buggy.v

```
                else if (requested_floor > current_floor)
                begin
                    current_floor = current_floor-1; -----------> moves down instead of up -----------> BUGGY
                    door=1'd0;
                    wait_floor=4'd0;
                    Up=1'd1;
                    Down=1'd0;
                end
```

After changing the Make file, the testbench is again simulated, and the output is as follows:

<img width="598" alt="image" src="https://user-images.githubusercontent.com/83169108/181640036-2031bad5-636c-4332-879c-7ddbf6ae59d9.png">

AS we can see, the design immediately fails as the elevator starts to move in the wrong direction.

## Verification Strategy

The Strategy is to check the following things:

- Moving in correct direcrion?
- Doors open or not?
- Correct floor reached? 

If all the testcases are passed for whole motion of the elevator, our verification is completed.
## Is the verification complete ?

Yes, the verification is completed, the same verification could be implemented for the elevator moving downwards using just an inverted for loop.
