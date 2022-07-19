//https://www.codewars.com/kata/514b92a657cdc65150000006/
object MultiplesOf3Or5 {
  def solution(number: Int): Long = (for (x <- 0L until number if x % 3 == 0 | x % 5 == 0) yield x).sum
}
