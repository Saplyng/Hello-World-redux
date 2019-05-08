import UIKit

import AVFoundation

var player: AVAudioPlayer?
var screams = ["willhelm","willhelm","willhelm","funnyAhh","funnyAhh","torture","femaleScream"]
var chosenScream = screams.randomElement()!
var chosenScream2 = screams.randomElement()!
var doubleRandom = {[$0,$1].randomElement()! as String}//closure?!

func playSound(randomString: String) {
    let url = Bundle.main.url(forResource: randomString, withExtension: "mp3")!
    
    do {
        print(randomString)
        player = try AVAudioPlayer(contentsOf: url)
        guard let player = player else { return }
        
        player.prepareToPlay()
        player.play()
    } catch let error {
        print(error.localizedDescription)
    }
}

playSound(randomString: doubleRandom(chosenScream,chosenScream2))



