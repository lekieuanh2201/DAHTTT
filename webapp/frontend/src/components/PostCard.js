import React from 'react'
import {AiOutlineLike} from 'react-icons/ai'
import {LiaCommentDotsSolid} from 'react-icons/lia'
import { format } from 'date-fns';

const PostCard = ({post, top}) => {
    const topNumber = top+1;
  return (
    <>
        <div className="card mb-3 post-card">
            <div className="row g-0">
                <div className="col-md-4 top-number-area">
                {/* <img src="" class="img-fluid rounded-start" alt="..."> */}
                    {/* <div className="overlay overlay_2" /> */}
                    <h1 className='top-number'>{topNumber}</h1> 
                </div>
                <div className="col-md-8">
                <div className="card-body">
                    {/* <button type="button" class="btn btn-primary button-detail">Detail</button> */}
                    <p className="card-text">{post.text.length > 100 ? post.text.substring(0, 100) + '...' : post.text}</p>
                    <div className='row'>
                        <div className='col-sm-4'>
                            <p class="card-text"><small class="text-muted">{format(new Date(Number(post.timestamp) * 1000), 'dd/MM/yyyy')}</small></p>
                        </div>
                        <div className='col-sm-4 d-flex like-number'>
                            <AiOutlineLike />
                            <p class="card-text"><small class="text-muted">{post.likes}</small></p>
                        </div>
                        <div className='col-sm-4 d-flex like-number'>
                            <LiaCommentDotsSolid />
                            <p class="card-text"><small class="text-muted">{post.comments}</small></p>
                        </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
    </>
  )
}

export default PostCard;