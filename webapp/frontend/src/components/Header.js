import React from 'react'
import {BsSearch} from 'react-icons/bs'
import {
  MDBIcon
} from 'mdb-react-ui-kit';
import { useLocation } from 'react-router-dom'; // Import useLocation from react-router-dom


const Header = () => {
  const location = useLocation();
  return (
    <header className='header sticky-top py-3 px-5'>
      <nav className='container-xxl'>
        <div className='row'>
          <div className='col-sm-4'>
            <a className='brand' href="/">
              <MDBIcon fab icon='facebook' size='lg'/>
              <h5 className='brand-text'>TrendingPosts</h5>
            </a>
          </div>
          <div className='col-sm-8 d-flex'>
            <form className='search-bar' >
              <input type="search"
                      className="search-input form-control me-2"
                      placeholder="Type to search"
                >
              </input>
              <button className="btn-search" type="submit" ><BsSearch /></button> 
            </form>
          </div>
        </div>
        <div className='nav-link-container row'>
          <div className='col-sm-6 text-end nav-link-div'>
              <a className= {`nav-link ${location.pathname === '/' ? 'active' : ''}`} aria-current="page" href="/">TRENDING POSTS</a>
          </div>
          <div className='col-sm-6 nav-link-div'>
            <a className= {`nav-link ${location.pathname === '/hot-topics' ? 'active' : ''}`} href="/hot-topics">HOT TOPICS</a>
          </div>
        </div>
      </nav>
      {/* <img src={headerphoto}/> */}
    </header>
  )
}

export default Header