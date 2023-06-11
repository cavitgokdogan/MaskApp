import express from "express"
import User from "../models/User.js"

const router = express.Router()

router.get("/",async(req,res)=>{
    const users = await User.find()
    res.json(users)
})


router.post("/",async(req,res)=>{
    const user = new User(req.body)
    await user.save()
    res.json("User has been created successfully")
})

router.put("/:id",async(req,res)=>{
    const user = await User.findByIdAndUpdate(req.params.id,req.body,{new:true})
    res.json(user)
})
router.delete("/:id",async(req,res)=>{
    await User.findByIdAndDelete(req.params.id)
    res.json("User has been deleted successfully")
})

export default router