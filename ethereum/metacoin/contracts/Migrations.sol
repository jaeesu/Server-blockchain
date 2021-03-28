// SPDX-License-Identifier: MIT
pragma solidity >=0.4.25 <0.7.0;

contract Migrations {
  address public owner;
  uint public last_completed_migration;

  modifier restricted() {
    if (msg.sender == owner) _;
  }
  ///@dev check if msg.sender is owner

  constructor() public {
    owner = msg.sender;
  }

  function setCompleted(uint completed) public restricted {
    last_completed_migration = completed;
  }
  ///@quest restricted 수식어??는 처음본다.
  ///@dev 마지막 migration 시간?을 입력 시간으로 변경??
}
