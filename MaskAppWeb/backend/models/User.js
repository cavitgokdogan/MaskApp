import mongoose from "mongoose";


const UserSchema = mongoose.Schema({
    name:{
        type:String,
        required:true
    },
    email:{
        type:String
    },
    number:{
        type:String
    },
    image:{
        type:String
    },
    cezapuani:{
        type:Number,
        default:0
    }
},{timestamps:true})

export default mongoose.model("User",UserSchema)