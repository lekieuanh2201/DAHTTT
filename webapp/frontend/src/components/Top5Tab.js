import React from "react";

import Tabs from "./Tabs";
import Panel from "./Panel";
import TopComment from "./TopComment";
import TopLike from "./TopLike";

function Top5Tab({topCommentedPosts, topLikedPosts}) {
  return (
    <Tabs>
      <Panel title="Most Comments">
      {topCommentedPosts.length > 0 ? (
              topCommentedPosts.map((post, index) => {
                return (
        <TopComment key={index} post={post}/>
        );
      })
      ) : (
        <h5>No posts found.</h5>
      )} 
      </Panel>
      <Panel title="Most likes">
      {topLikedPosts.length > 0 ? (
              topLikedPosts.map((post, index) => {
                return (
        <TopLike key={index} post={post}/>
        );
      })
      ) : (
        <h5>No posts found.</h5>
      )} 
      </Panel>
    </Tabs>
  );
}
export default Top5Tab;
