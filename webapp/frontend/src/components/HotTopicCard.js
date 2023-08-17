import React from 'react'
import {AiOutlineLike} from 'react-icons/ai'
import {LiaCommentDotsSolid} from 'react-icons/lia'

const HotTopicCard = ({topic, index}) => {
    const topNumber = index + 1;
  return (
    <>
        <div className="card mb-3 hot-topic-card">
            <div className="row g-0">
                <div className="col-md-4 top-number-area">
                {/* <img src="" class="img-fluid rounded-start" alt="..."> */}
                    {/* <div className="overlay overlay_2" /> */}
                    <h1 className='top-number'>{topNumber}</h1> 
                </div>
                <div className="col-md-8">
                <div className="card-body">
                    <h5 class="card-title">{topic}</h5>
                    {/* <p className="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p> */}
                    {/* <div className='row'>
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
                    </div> */}
                </div>
                </div>
            </div>
            </div>
    </>
  )
}

export default HotTopicCard