//
//  VaccineSearch.swift
//  
//
//  Created by student on 5/5/19.
//

import Foundation

import UIKit


var dataTask: URLSessionDataTask?

struct Vaccine: Decodable {
    let name: String?
    let category: Array <String>?
    let administration: String?
    let contraindications: String?
    let pdf: String?
    
    //    enum CodingKeys : String, CodingKey {
    //        case name, administration, contraindications, pdf
    //        case category = "Category"
    //    }
}

public func searchedVaccine(userSearch: String) {
    dataTask?.cancel()
    let jsonUrlString = "http://jstein.mccdgm.net/blog/json/vaccinesV2.json"
    
    guard let url = URL(string: jsonUrlString) else {  return }
    
    URLSession.shared.dataTask(with: url) { (data, resonse, err) in
        guard let data = data else {return}
        
        do {
            let vaccine = try JSONDecoder().decode([Vaccine].self, from: data)
            
            var vaccineList: Array <String> = []
            for shot in vaccine {
                vaccineList.append(shot.name!)
            }
            
            if let index = vaccineList.firstIndex(of: userSearch){
                print(vaccine[index].name!)
                print("Category: \(vaccine[index].category!)")
                print("")
                print("Contraindications:")
                print(vaccine[index].contraindications!)
                print("")
                print("Administration:")
                print(vaccine[index].administration!)
                print("")
                print("Link to package insert:")
                print(vaccine[index].pdf!)
            } else {
                print("some error occured")
            }
            
            
            
            
            
        } catch let jsonErr {
            print("error serializing json", jsonErr)
        }
        
        }.resume()
}


public func orderedVaccines() {
    dataTask?.cancel()
    let jsonUrlString = "http://jstein.mccdgm.net/blog/json/vaccinesV2.json"
    
    guard let url = URL(string: jsonUrlString) else {  return }
    
    URLSession.shared.dataTask(with: url) { (data, resonse, err) in
        guard let data = data else {return}
        
        do {
            let vaccine = try JSONDecoder().decode([Vaccine].self, from: data)
            
            var vaccineList: Array <String> = []
            
            for shot in vaccine {
                vaccineList.append(shot.name!)
            }
            
            vaccineList.sort()
            
            for shot in vaccineList {
                print(shot)
            }
            
        } catch let jsonErr {
            print("error serializing json", jsonErr)
        }
        
        }.resume()
}
