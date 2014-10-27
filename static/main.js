/* global $, remark, TweetPanel, ProgressPanel  */

$(function () {
  'use strict';
  var slideshow = remark.create({
    sourceUrl: 'slide.md',
    ratio: '4:3',
    highlightLanguage: 'python',
    highlightStyle: 'github'
  });
  var progressPanel = new ProgressPanel($("#progress-panel"), {
    timer: {
      limit: (5 * 60 * 1000),
    },
    page: {
      total: slideshow.getSlideCount(),
      current: slideshow.getCurrentSlideNo()
    }
  });
  var tweetPanel = new TweetPanel($('#tweet-panel'));

  slideshow.on('showSlide', progressPanel.showSlideHandler());

  $(window).on('resize', function () {
    tweetPanel.resize();
    progressPanel.resize();
  });

  var ws = new WebSocket('ws://localhost:3000/search');
  ws.onmessage = function (e) {
    var msg = JSON.parse(e.data);
    tweetPanel.add(msg);
  };
  $(window).unload(function () {
    ws.close();
    ws = null;
  });
});

// vi:set sts=2 sw=2 et:
