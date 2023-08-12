import React from 'react'
import {AiOutlineLike} from 'react-icons/ai'
import {LiaCommentDotsSolid} from 'react-icons/lia'
const PostCard = () => {
  return (
    <>
        <div className="card mb-3 post-card">
            <div className="row g-0">
                <div className="col-md-4 top-number-area">
                {/* <img src="" class="img-fluid rounded-start" alt="..."> */}
                    {/* <div className="overlay overlay_2" /> */}
                    <h1 className='top-number'>1</h1> 
                </div>
                <div className="col-md-8">
                <div className="card-body">
                    <button type="button" class="btn btn-primary button-detail">Detail</button>
                    <p className="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    <div className='row'>
                        <div className='col-sm-4'>
                            <p class="card-text"><small class="text-muted">23/07/2023</small></p>
                        </div>
                        <div className='col-sm-4 d-flex like-number'>
                            <AiOutlineLike />
                            <p class="card-text"><small class="text-muted">1234</small></p>
                        </div>
                        <div className='col-sm-4 d-flex like-number'>
                            <LiaCommentDotsSolid />
                            <p class="card-text"><small class="text-muted">5678</small></p>
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