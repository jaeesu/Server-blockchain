centralized scrooge : 사용자로부터 트랜잭션을 수신
transaction : 기간또는 block으로 구성
class :
	scrooge coin transaction class
	transaction class having inner class(input, output...)
output :
	(pk, value)
	pk : Java PublicKey class
input :
	hash, index, signature

to make input verified, signature in input is verifing about 현재 트랜잰셕.

signatured raw data : getRawDataToSing(int index) method
check the signature : verifySignature() - Crypto.java
public static boolean checkSignature(PublicKey pubKey, byte[] msg, byte[] sig)
	공용키, 메시지 및 서명, 서명만 공용키를 사용해 메시지를 올바르게 확인하는 경우 true를 반환

서명 계산은 적절한 개인키를 알고 있는 엔티티에 의해 트랜잭션 클래스 외부에서 수행된다.

transaction : input list, output list, unique id(getRawTx())
	클래스는 또한 입력을 추가 및 제거하고, 출력을 추가하고, 다이제스트를 부호/해시에 계산하고, 서명을 입력에 추가하고, 모든 입력/출력/서명이 추가되면 트랜잭션의 해시를 계산하고 저장하는 방법을 포함합니다.

UTXO class : 처리되지 않은 트랜잭션 출력(해당 트랜잭션 index, hash)
	동일한 해시 코드와 비교 함수, 해당 인덱스와 txHash array의 내용을 기반으로 두 UTXO 간의 동일성과 비교를 가능하게 한다.
	미결 UTXO의 현재 집합을 나타내고, 해당 트랜책션 출력 매핑을 포함하는 utxo pull? class 
빈 UTXOPool, 지정된 UTXOPool 복사본을 만드는 생성자 포함, pool에서 utxo 추가, 제거, 출력, 풀에 있는지 확인, 전체 목록 가져옴

You will be responsible for creating a file called TxHandler.java that implements the following API:
public class TxHandler {

  /** Creates a public ledger whose current UTXOPool 
    * (collection of unspent transaction outputs) is utxoPool. 
    * This should  make a defensive copy of utxoPool by using 
    * the UTXOPool (UTXOPool uPool) constructor.
    */
  public TxHandler(UTXOPool utxoPool);

  /** Returns true if
   * (1) all outputs claimed by tx are in the current UTXO pool
   * (2) the signatures on each input of tx are valid
   * (3) no UTXO is claimed multiple times by tx
   * (4) all of tx’s output values are non-negative
   * (5) the sum of tx’s input values is greater than or equal 
   * to the sum of its output values; and false otherwise.
   */
  public boolean isValidTx(Transaction tx);

  /** Handles each epoch by receiving an unordered array of 
   * proposed transactions, checking each transaction for 
   * correctness, returning a mutually valid array of accepted 
   * transactions, and updating the current UTXO pool as 
   * appropriate.
   */
  public Transaction[] handleTxs(Transaction[] possibleTxs);

}

handleTxs() : return 최대 크기의 상호 유효한 트랜잭션 세트, 최대 크기 집합을 계산할 필요는 없다.
	수락하기로 선택한 트랜잭션을 기반으로 내부 UTXOPool을 업데이트하여 현재 미사용 트랜잭션 출력 집합을 반영

isValidTx()

MaxFeeTxHandler.java


library :
	java.security.Signature
		어플리케이션에 대해 디지털 서명 알고리즘의 기능을 제공하기 위해 사용.
		디지털 서명 : 인증이나 디지털 데이터의 무결성을 보증하기 위해 사용ㅑ
		getInstance : 
	http://cris.joongbu.ac.kr/course/2018-1/jcp/api/java/security/Signature.html
