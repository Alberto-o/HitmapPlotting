/*
 *  XmlStreamer.h
 *  Formatter
 *
 *  Created by sroe on 12/01/2010.
 *  Copyright 2010 CERN. All rights reserved.
 *
 */
#ifndef XmlStreamer_h
#define XmlStreamer_h

#include "IElementStreamer.h"

namespace SCT_CalibAlgs{
class XmlStreamer:public IElementStreamer{
public:
  XmlStreamer(const std::string & name, const std::map<std::string, std::string> & attributes, std::ostream & os=std::cout);
  XmlStreamer(const std::string & name, const std::string & attributeName, const std::string & attributeValue, std::ostream & os=std::cout);
  
  XmlStreamer(const std::string & name, const std::vector<std::string> & attributeNames, const std::vector<std::string> & attributeValues, std::ostream & os=std::cout);
  XmlStreamer(const std::string & name, std::ostream & os=std::cout);
  virtual ~XmlStreamer();
};

}
#endif
