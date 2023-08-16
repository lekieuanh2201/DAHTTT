import React from 'react'
import {AiOutlineLike} from 'react-icons/ai'
import {LiaCommentDotsSolid} from 'react-icons/lia'
import { format } from 'date-fns';

const TopLike = ({post}) => {
  return (
    <div className='card mb-3 top-comment'>
      <div className="card-body">
          {/* <button type="button" class="btn btn-primary button-detail">Detail</button> */}
          <p className="card-text">{post.text.length > 100 ? post.text.substring(0, 100) + '...' : post.text}</p>
          <div className='row'>
              <div className='col-sm-6'>
                  <p class="card-text"><small class="text-muted">{format(new Date(Number(post.timestamp) * 1000), 'dd/MM/yyyy')}</small></p>
              </div>
              <div className='col-sm-6 d-flex like-number'>
                  <AiOutlineLike />
                  <p class="card-text"><small class="text-muted">{post.likes}</small></p>
              </div>
          </div>
      </div>
    </div>

  )
}

export default TopLike