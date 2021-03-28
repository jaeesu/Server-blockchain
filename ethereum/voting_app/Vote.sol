
pragma solidity >=0.4.23 <0.7.0;

contract Vote{
    
    //structure(candidator)
    struct candidator{
        string name;
        uint upVote;
    }
    
    //variable
    candidator[] public candidatorList;
    bool live;
    address owner;
    
    //mapping
    mapping(address => bool) Voted;
    
    //modifier
    modifier onlyOwner{
        require(msg.sender == owner);
        _;
    }
    
    //constructor
    constructor() public {
        owner = msg.sender;
        live = true;
        
        emit Voting(owner);
    }
    
    //event
    event AddCandidator(string name);
    event UpVote(string candidator, uint upVote);
    event FinishVote(bool live);
    event Voting(address owner);
    
    
    
    //기능 정리
    //1.후보자 등록(condidator)
    function addCandidator(string memory _name) public onlyOwner {
        require(live == true);
        require(candidatorList.length < 5);
        candidatorList.push(candidator(_name, 0));
        //무제한무제무 등등록x
        
        
        //emit event
        emit AddCandidator(_name);
        
    }
    
    //2.후보자 확인(get condidator)
    //getter 사용

    //3.투표
    function upVote(uint _indexOfCandidator) public {
        require(live == true);
        require(_indexOfCandidator < candidatorList.length);
        require(Voted[msg.sender] == false); //must i init before using it?
        candidatorList[_indexOfCandidator].upVote++;
        
        Voted[msg.sender] = true;
        
        emit UpVote(candidatorList[_indexOfCandidator].name, candidatorList[_indexOfCandidator].upVote);
        //afet voting, can't voting 

    }

    //4.투표 종료
    function finishVote() public onlyOwner {
        require(live == true);
        //alive vote?
        live = false;
        emit FinishVote(live);
        //public - everyone can close -> only msg,sender
        
    }

}
