import React from 'react'
import {AiOutlineLike} from 'react-icons/ai'
import {LiaCommentDotsSolid} from 'react-icons/lia'
const TopLike = () => {
  return (
    <div className='card mb-3 top-comment'>
      <div className="card-body">
          <button type="button" class="btn btn-primary button-detail">Detail</button>
          <p className="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          <div className='row'>
              <div className='col-sm-6'>
                  <p class="card-text"><small class="text-muted">23/07/2023</small></p>
              </div>
              <div className='col-sm-6 d-flex like-number'>
                  <AiOutlineLike />
                  <p class="card-text"><small class="text-muted">1234</small></p>
              </div>
          </div>
      </div>
    </div>

  )
}

export default TopLike