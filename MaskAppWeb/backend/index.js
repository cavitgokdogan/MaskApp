import express from "express"
import cors from "cors"
import dotenv from "dotenv"
import mongoose from "mongoose"
import userRoutes from "./routes/users.js"
const app = express()
dotenv.config()


mongoose.connect(process.env.MONGO_URL || 5000).then(() => {
    console.log("Connected to DB")
}).catch((err)=>{
    console.log(err)
})

app.use(cors())
app.use(express.json()) // json formatındaki gelen body'lerini handle etmeyi sağlar.


app.listen(process.env.PORT,()=>{
    console.log("Server is running")
})

app.use("/users",userRoutes)
