import React from 'react';
import { Card, CardActions, CardContent, CardMedia, Button, Typography } from '@material-ui/core/';
import ThumbUpAltIcon from '@material-ui/icons/ThumbUpAlt';
import DeleteIcon from '@material-ui/icons/Delete';
import MoreHorizIcon from '@material-ui/icons/MoreHoriz';
import useStyles from './styles';

const StudentCard = ({student}) => {
    const classes = useStyles()
  return (
    <Card className={classes.card}>
      <CardMedia className={classes.media} image={student.image} />
      <div className={classes.overlay}>
        <Typography variant="h6">{student.name}</Typography>
      </div>
      <div className={classes.overlay2}>
        <Button style={{ color: 'white' }} size="small"><MoreHorizIcon fontSize="default" /></Button>
      </div>
      <div className={classes.details}>
        <Typography variant="body2" color="textSecondary" component="h2">{student.email}</Typography>
      </div>
      <Typography className={classes.title} gutterBottom variant="h5" component="h2">Ceza puani:{student.cezapuani}</Typography>
      <CardContent>
        <Typography variant="body2" color="textSecondary" component="p">{student.number}</Typography>
      </CardContent>
    </Card>
  )
}

export default StudentCard