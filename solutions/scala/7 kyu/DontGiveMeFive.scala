//https://www.codewars.com/kata/5813d19765d81c592200001a
object Sol {
  def dontGiveMeFive(start: Int, end: Int): Int = {
    (start to end).filter(x => !(x.toString contains '5')).length
  }
}