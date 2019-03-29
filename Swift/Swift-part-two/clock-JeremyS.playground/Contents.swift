import UIKit
import Darwin

let formatter = DateFormatter()
formatter.dateFormat = "HH:mm:ss"

func recurrsionClock(){
    DispatchQueue.main.asyncAfter(deadline: .now() + 0.97){
        print(formatter.string(from: Date()) + "\r")
        fflush(stdout)
        recurrsionClock()
    }
}
recurrsionClock()








