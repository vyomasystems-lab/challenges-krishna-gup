# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_fsm_bug1(dut):

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


