//https://www.codewars.com/kata/542c0f198e077084c0000c2e/
object Sol {

  def divisors(n: Int): Int = {
    (1 to n / 2).filter(x => n % x == 0).size + 1
  }

}