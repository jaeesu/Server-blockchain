const helloWorld = artifacts.require("HelloWorld");

//HelloWorld는 파일명이 아니라 컨트랙트 이름
//한 소스 파일에 컨트랙트가 여러 개일 수 있으므로 무의미

module.exports = function(deployer){
	deployer.deploy(helloWorld, "Hello, World!");
};

