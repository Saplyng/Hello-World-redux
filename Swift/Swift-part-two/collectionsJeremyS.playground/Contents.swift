import UIKit


//so this would be a dictionary with arrays as values
var instruments = ["guitars" : ["Harly Benton Les Paul", "Squire P-Bass", "Epiphone Sheritan", "Squire Telecaster", "Takamine G-series", "Cortez 12-String"],
    "precussion" : ["Tama drum set", "cajon drum"],
    "pianos" : ["Yamaha baby grand piano", "Korg keyboard", "Yamaha digital piano"],
    "other": ["Kazoo", "Harmonica", "Spoons", "Ukulele", "Mandolin", "flute", "tin whistle", "tibetan singing bowl"]]


func randomBand(){
    var bandInstruments = [String]()
    for type in instruments.values{
        bandInstruments.append(type.randomElement()!)
    }
    print("We'll make a band with a \(bandInstruments[0]), a \(bandInstruments[1]), a \(bandInstruments[2]), and a \(bandInstruments[3])")
}
randomBand()

