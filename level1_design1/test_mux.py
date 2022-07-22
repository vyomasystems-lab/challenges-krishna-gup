# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    # input driving
    
    x = 0
    dut.sel.value = x
    dut.inp0.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp0.value} model={dut.inp0.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp0.value, "Randomised test failed"

    x = 1
    dut.sel.value = x
    dut.inp1.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp1.value} model={dut.inp1.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp1.value, "Randomised test failed"

    x = 2
    dut.sel.value = x
    dut.inp2.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp2.value} model={dut.inp2.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp2.value, "Randomised test failed"

    x = 3
    dut.sel.value = x
    dut.inp3.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp3.value} model={dut.inp3.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp3.value, "Randomised test failed"

    x = 4
    dut.sel.value = x
    dut.inp4.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp4.value} model={dut.inp4.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp4.value, "Randomised test failed"

    x = 5
    dut.sel.value = x
    dut.inp5.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp5.value} model={dut.inp5.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp5.value, "Randomised test failed"

    x = 6
    dut.sel.value = x
    dut.inp6.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp6.value} model={dut.inp6.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp6.value, "Randomised test failed"

    x = 7
    dut.sel.value = x
    dut.inp7.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp7.value} model={dut.inp7.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp7.value, "Randomised test failed"

    x = 8
    dut.sel.value = x
    dut.inp8.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp8.value} model={dut.inp8.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp8.value, "Randomised test failed"

    x = 9
    dut.sel.value = x
    dut.inp9.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp9.value} model={dut.inp9.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp9.value, "Randomised test failed"

    x = 10
    dut.sel.value = x
    dut.inp10.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp10.value} model={dut.inp10.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp10.value, "Randomised test failed"

    x = 11
    dut.sel.value = x
    dut.inp11.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp11.value} model={dut.inp11.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp11.value, "Randomised test failed"

    x = 12
    dut.sel.value = x
    dut.inp12.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp12.value} model={dut.inp12.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp12.value, "Randomised test failed"

    x = 13
    dut.sel.value = x
    dut.inp13.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp13.value} model={dut.inp13.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp13.value, "Randomised test failed"

    x = 14
    dut.sel.value = x
    dut.inp14.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp14.value} model={dut.inp14.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp14.value, "Randomised test failed"

    x = 15
    dut.sel.value = x
    dut.inp15.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp15.value} model={dut.inp15.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp15.value, "Randomised test failed"

    x = 16
    dut.sel.value = x
    dut.inp16.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp16.value} model={dut.inp16.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp16.value, "Randomised test failed"

    x = 17
    dut.sel.value = x
    dut.inp17.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp17.value} model={dut.inp17.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp17.value, "Randomised test failed"

    x = 18
    dut.sel.value = x
    dut.inp18.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp18.value} model={dut.inp18.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp18.value, "Randomised test failed"

    x = 19
    dut.sel.value = x
    dut.inp19.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp19.value} model={dut.inp19.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp19.value, "Randomised test failed"

    x = 20
    dut.sel.value = x
    dut.inp20.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp20.value} model={dut.inp20.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp20.value, "Randomised test failed"

    x = 21
    dut.sel.value = x
    dut.inp21.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp21.value} model={dut.inp21.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp21.value, "Randomised test failed"

    x = 22
    dut.sel.value = x
    dut.inp22.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp22.value} model={dut.inp22.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp22.value, "Randomised test failed"

    x = 23
    dut.sel.value = x
    dut.inp23.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp23.value} model={dut.inp23.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp23.value, "Randomised test failed"

    x = 24
    dut.sel.value = x
    dut.inp24.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp24.value} model={dut.inp24.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp24.value, "Randomised test failed"

    x = 25
    dut.sel.value = x
    dut.inp25.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp25.value} model={dut.inp25.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp25.value, "Randomised test failed"

    x = 26
    dut.sel.value = x
    dut.inp26.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp26.value} model={dut.inp26.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp26.value, "Randomised test failed"

    x = 27
    dut.sel.value = x
    dut.inp27.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp27.value} model={dut.inp27.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp27.value, "Randomised test failed"

    x = 28
    dut.sel.value = x
    dut.inp28.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp28.value} model={dut.inp28.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp28.value, "Randomised test failed"

    x = 29
    dut.sel.value = x
    dut.inp29.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp29.value} model={dut.inp29.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp29.value, "Randomised test failed"

    x = 30
    dut.sel.value = x
    dut.inp30.value = random.randint(0,3)
    await Timer(2, units='ns')
    dut._log.info(f'SEL={dut.sel.value} IN={dut.inp30.value} model={dut.inp30.value} DUT={int(dut.out.value)}')
    assert dut.out.value == dut.inp30.value, "Randomised test failed"
