import React from 'react';
import { Grid } from '@material-ui/core';
import axios from "axios"
import useStyles from './styles';
import StudentCard from '../StudentCard/StudentCard';
import { useEffect, useState } from "react";


const Students = () => {
    const [students, setStudents] = useState([])
    const fetchUsers = async () => {
        const { data } = await axios.get(process.env.REACT_APP_API_URL+"/users")
        console.log(data)
        setStudents([...data])
    }
    useEffect(() => {
        fetchUsers()
    }, [])
    const classes = useStyles()
    return (
        <Grid className={classes.container} container alignItems="stretch" spacing={3}>
            {
                students.map((student)=>(
                    <Grid item xs={6} sm={4} md={4}>
                        <StudentCard student={student}/>
                    </Grid>
                ))
            }
        </Grid>
    )
}

export default Students