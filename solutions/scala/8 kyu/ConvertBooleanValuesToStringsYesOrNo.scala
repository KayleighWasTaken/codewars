//https://www.codewars.com/kata/53369039d7ab3ac506000467/
object Kata {

  def boolToWord(boolean: Boolean): String = boolean match{
    case true => "Yes"
    case false => "No"
  }

}