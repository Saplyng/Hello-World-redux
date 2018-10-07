class BaseCharacter{

    enum Allegiance{
        case pc
        case npc
        case enemy
    }

    var name : String?
    var level : Int?
    var hp : Int?
    var mp : Int?
    var location : String?
    var fealty : Allegiance?
    var image : String? //img/person.png

    init(_ name: String?, _ level:Int?, _ hp:Int?, _ mp:Int?, _ location:String?, _ fealty:Allegiance?, _ image: String?) {
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.location = location
        self.fealty = fealty
        self.image = image
    }

    func describe() -> String {
        return """
            Name: \(name!)
            level: \(level!)
            hp: \(hp!)
            mp: \(mp!)
            fealty: \(fealty!)
            image: \(image!)
            """
    }
}

let pc1 = BaseCharacter("Suzie", 3, 21, 30, "Dunwall", .pc,"")
print(pc1.describe())
