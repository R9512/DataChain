pragma solidity <0.9.0;
contract Sairam
 {
    event Created(string msg);
    mapping(uint256 => User) users;
    string private message = "Swami";
    struct User 
    {
        uint256 id;
        string[] data;
        bool isDone;
    }
    function newUser(uint256 _id,string memory _modid, string memory _userid, string memory _sign,string memory _proof) public 
    {

        message="NotDone";
        if(keccak256(abi.encodePacked(_sign))==keccak256(abi.encodePacked(_proof)))
        {
            if(users[_id].isDone==false)
            {

                users[_id].id = _id;
                users[_id].isDone=true;
                users[_id].data.push(_modid);
                users[_id].data.push(_userid);
                message="Done";
                emit Created("0");//For Created
            }
        }

    }
    function saySairam() public pure returns (string memory)
    {
        return("Sairam");
    }
    function setData(uint256 _id, uint256 _index, string memory _newData) public 
    {
        users[_id].data[_index] = _newData;
    }
    function getUserData(uint256 _id, uint256 _dataIndex) public view returns (string memory)
    {
        return users[_id].data[_dataIndex];
    }

    function getDataSize(uint256 _id) public view returns (uint256) 
    {
        return users[_id].data.length;        
    }

    function getMessage() public view returns(string memory)
    {
        return(message);
    }
}