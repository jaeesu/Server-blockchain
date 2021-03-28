//1.reset candidator -> constructor - @param all name of candidator
//2.vote candidator
//3.check the upvote for each candidator

pragma solidity >= 0.4.23;

//contract is class in other language.
contract Voting {
    //1.construcotr to intialize candidates
    //2. vote for candidates
    //3.get count of voted for each candidates
    
    string[] public candidateList;
    //연연관연관뱅연관배열 햇해쉬
    mapping (string => uint8) public votesReceived;
    
    constructor(string[] storage candidateNames) public {
        //byte - solidity does not support string or array?? old ??
        //each candidate assign to variable
        candidateList = candidateNames;
        //public : 욉외부 접접근 간가능
        //when deploy?? only one init
        //many deployes same code - just making each other instances on blockchain
        //save upvote
    }
    
    function voteForeCandidate(string memory candidate) public {
        require(validCandidate(candidate));
        votesReceived[candidate]++;
        //don't need to init 0
        
    }
    
    function totalVotesFor(string memory candidate) view public returns(uint8){
        require(validCandidate(candidate));
        return votesReceived[candidate];
    }
    //view - only read
    
    //check if a valid candidate
    function validCandidate(string memory candidate) view public returns(bool){
        for(uint i=0; i<candidateList.length; i++){
            if(candidateList[i] == candidate){
                return true;
            }
            return false;
        }
    }
    //can use 곗계속, 윻유횩유효검유효검사유효검사용유효검사용을유효검사용으로
}
