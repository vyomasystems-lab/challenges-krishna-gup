# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

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
    
    
    assert dut.seq_seen.value == 1, "Passed"


