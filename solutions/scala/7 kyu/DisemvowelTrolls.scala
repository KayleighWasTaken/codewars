//https://www.codewars.com/kata/52fba66badcd10859f00097e
object Sol {
  def disemvowel(str: String): String = {
    str.filter(c => !("aeiouAEIOU" contains c))
  }
}