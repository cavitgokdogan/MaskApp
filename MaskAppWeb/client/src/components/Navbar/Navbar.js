import { AppBar, Typography, Toolbar, Avatar, Button } from '@material-ui/core';
import React from 'react'
import useStyles from './styles.js';

const Navbar = () => {
    const classes = useStyles()
    return (
        <AppBar className={classes.appBar} position="static" color="inherit">
            <Typography className={classes.heading} variant="h2" align="center">List of suspended</Typography>
            <img className={classes.image} src="https://d2gg9evh47fn9z.cloudfront.net/800px_COLOURBOX8384293.jpg" alt="icon" height="60" />
        </AppBar>
    )
}

export default Navbar