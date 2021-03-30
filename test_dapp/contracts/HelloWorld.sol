pragma solidity >= 0.4.23;

contract HelloWorld {
	string public greeting;

	constructor(string memory _greeting) public {
		greeting = _greeting;
	}

	function setGreeting(string memory _greeting) public {
		greeting = _greeting;
	}

	function say() public view returns(string memory){
		return greeting;
	}
}

