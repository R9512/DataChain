
pragma solidity <0.9.0;
contract Hello
{
    string public message;
    constructor(string memory _message)
    {
        message = _message;
    }

    function hello() public view returns(string memory) 
    {
        return message;
    }

    function sethello(string memory _message) public payable
    {
       // require(msg.value>1 ether);
        message = _message;
    } 
}