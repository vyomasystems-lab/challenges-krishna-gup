# Bit Manipulation Co Processor Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

<img width="735" alt="image" src="https://user-images.githubusercontent.com/83169108/180520436-6741d501-6f8c-4fd8-961e-7fac0aeaeb7f.png">

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test.
The values are assigned to the input port using 

```

    ins = [0x40007033, 0x40006033, 0x40004033, 0x20001033, 0x20005033, 0x20002033, 0x20004033, 0x20006033, 
        0x60001033, 0x60005033, 0x48001033, 0x48005033, 0x48006033, 0x48004033, 0x48007033, 0x28001033, 0x28005033,
        0x68001033, 0x68005033, 0x0A001033, 0x0A003033, 0x0A002033, 0x0A004033, 0x0A005033, 0x0A006033, 
        0x0A007033, 0x08006033, 0x08004033, 0x08007033, 0x08001033]

    for i in ins:
        mav_putvalue_src1 = 0x5
        mav_putvalue_src2 = 0x0
        mav_putvalue_src3 = 0x0
        mav_putvalue_instr = i

    # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
  
        yield Timer(1) 

    # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message

```

The design is checked at all possible combinations of the instruction bits. As stated in the Model, and the output is compared with the desired output.

<img width="594" alt="image" src="https://user-images.githubusercontent.com/83169108/181638122-5a2d6adc-7042-43a4-a0b4-3bcc61890402.png">

We can see that when the instruction is for ADDN, the output dosen't match with the desired output. Hence a BUG is present here.

## Test Scenario

- Test Inputs: All possible combinations of instructions
- Expected Output: According to the Model of Processor
- Observed Output: In case of ADDN instruction, output is not correct

Output mismatches for the above inputs proving that there is a design bug

## Is the verification complete ?

Yes, the verification is completed
