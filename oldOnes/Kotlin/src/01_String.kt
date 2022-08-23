import java.util.*
import kotlin.collections.ArrayList

fun main(){
    val temp1: String = "Hi"
    val temp2: String = "Kotlin"
    val temp3: String = "This is For Loop"
    var arrayList = ArrayList<String>()
    arrayList.add(temp1)
    arrayList.add(temp2)
    arrayList.add(temp3)
    for (s in arrayList){
        println(s)
        if (s == arrayList.get(arrayList.size - 1)) {
            println(arrayList.size)
        }
    }



}
