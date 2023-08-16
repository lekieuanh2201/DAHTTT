import {React, useEffect, useState} from 'react'
import photo from '../img/headerphoto.png'
import top10 from '../img/Component 1.png'
import top5 from '../img/Component 2.png'
import DatePicker from "react-datepicker";
import PostCard from '../components/PostCard';
import Top5Tab from '../components/Top5Tab';
import axios from 'axios';
import data from '../data_posts.json';
import { useLocation } from 'react-router-dom';
import PostCardSearch from '../components/PostCardSearch';


const Home = () => {
  
  const [startDate, setStartDate] = useState();
  const [endDate, setEndDate] = useState();
  
  //load data from db using api
  const [data, setData] = useState([]);
  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const result = await axios.get("http://localhost:8000/get_trending_posts/");
      setData(result.data.post_texts);
    // console.log(result.data)
    } catch (error) {
      console.error("Error loading data:", error);
    }
  
  }

  
  const posts = data

  // filter post to date
  const filteredPosts = posts.filter(post => {
  
    if (startDate && endDate) {
      return post.timestamp*1000 >= startDate.getTime() && post.timestamp*1000 <= endDate.getTime(); 
    }
    return true;
  });


// top 5 likes
  const topLikedPosts = filteredPosts
    .sort((a, b) => b.likes - a.likes)
    .slice(0, 5);

  // top 5 comment
  const topCommentedPosts = filteredPosts
    .sort((a, b) => b.comments - a.comments)
    .slice(0, 5);
  
  // top 10
  const postsWithEngagement = filteredPosts.map(post => ({
    ...post,
    engagement: post.likes + post.comments,
  }));
  
  const topEngagementPosts = postsWithEngagement
    .sort((a, b) => b.engagement - a.engagement)
    .slice(0, 10);

  
  // handle search
  const location = useLocation();
  const searchQuery = new URLSearchParams(location.search).get('q') || '';
  

  const searchPosts = posts.filter((post) =>
    post.text.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <>
    
      <div className='image_wrapper'>
        <img className='img-header' src={photo} alt='header photo'/>
        <div class="overlay overlay_2">
        <h1>What's new today?</h1> 
      </div>
      
      </div>
      {searchQuery.length > 0 ? (
      searchPosts.map((post, index) => {
        return (
          <>
          <div className='post-search-area'>
            <PostCardSearch post={post} key={index} top={index} />
          </div>
          </>
          );
        })
        ) : (
      <>
      <div className='date-picker d-flex'>
        <h7>From </h7>
        <DatePicker
          selectsStart
          selected={startDate}
          onChange={date => setStartDate(date)}
          startDate={startDate}
          className='input-date'
        />
        <h7> to </h7>
        <DatePicker
          selectsEnd
          selected={endDate}
          onChange={date => setEndDate(date)}
          endDate={endDate}
          startDate={startDate}
          minDate={startDate}
          className='input-date'
      />
      </div>
      <div className='row top-posts-container'>
        <div className='col-sm-8 top10-container'>
          <img src={top10} className='top10-title'/>
          <div className='top10-postcard-container'>
          {topEngagementPosts.length > 0 ? (
              topEngagementPosts.map((post, index) => {
                return (
            <PostCard post={post} key={index} top={index}/> 
             );
          })
          ) : (
            <h5>No posts found.</h5>
          )} 
          </div>
        </div>
        <div className='col-sm-4'>
          <img src={top5} className='top5-title'/>
          <Top5Tab topLikedPosts={topLikedPosts} topCommentedPosts={topCommentedPosts}/>
        </div>
      </div>
      </>
      )} 
    </>
  )
}

export default Home